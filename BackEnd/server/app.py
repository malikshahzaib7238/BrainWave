from flask import send_file
import io
import pymysql
import os
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import requests
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})  

host = 'localhost'
user = 'root'
password = 'zaq@12wsx'
database = 'eeg-app'


def create_connection():
    return pymysql.connect(host=host, user=user, password=password, database=database)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if not os.path.exists('temp_files'):
            os.makedirs('temp_files')

        print("This function is now called")
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request.'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file.'}), 400

        if file:
            model_api_url = 'http://localhost:9000/predict'  # Replace with the actual model API URL
            files = {'file': (file.filename, file)}
            response = requests.post(model_api_url, files=files)
            filename = secure_filename(file.filename)
            # Save the file to the 'temp_files' directory
            file_path = os.path.join('temp_files', filename)
            file.save(file_path)
            prediction = response.json()['prediction']
            # Save the EDF file content to the 'eegdata' table
            try:
                connection = create_connection()
                cursor = connection.cursor()

                with open(file_path, 'rb') as edf_file:
                    file_content = edf_file.read()

                sql = "INSERT INTO eegdata (file, prediction) VALUES (%s, %s)"
                if prediction == 0:
                    content = "Normal"
                else:
                    content = "Abnormal"
                cursor.execute(sql, (file_content, content))
                connection.commit()

                cursor.close()
                connection.close()
                os.remove(file_path)
            except pymysql.Error as e:
                return jsonify({'error': 'Error saving data to the database.'}), 500
            if prediction == 0:
                return jsonify({'prediction': 'Your Report is Normal'}), 200
            else:
                return jsonify({'prediction': 'Your Report is Abnormal'}), 200
        else:
            return jsonify({'error': 'Error while processing the file.'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred during processing: ' + str(e)}), 500


@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if name and email and message:
        try:
            # Create the folder if it doesn't exist
            if not os.path.exists('contactData'):
                os.makedirs('contactData')

            with open('contactData/form-data.txt', 'a') as file:
                file.write(
                    f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")
            return jsonify({'message': 'Form data submitted successfully.'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Incomplete form data.'}), 400


@app.route('/login_doctor', methods=['POST'])
def login_doctor():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']

        try:
            connection = create_connection()
            cursor = connection.cursor()

            sql = "SELECT * FROM doctor WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except pymysql.Error as e:
            return jsonify({"error": "Login failed"}), 500


@app.route('/view', methods=['GET'])
def view_edf_files():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        sql = "SELECT `No.`, `File`, `Prediction` FROM eegdata"
        cursor.execute(sql)
        edf_files = [{"No": row[0], "Prediction": row[2]}
                     for row in cursor.fetchall()]

        cursor.close()
        connection.close()

        return jsonify({"edf_files": edf_files}), 200

    except pymysql.Error as e:
        print("Database Error:", e)
        return jsonify({"error": "Failed to retrieve EDF files: " + str(e)}), 500


@app.route('/download/<file_no>', methods=['GET'])
def download_file(file_no):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        sql = "SELECT `File` FROM eegdata WHERE `No.` = %s"
        cursor.execute(sql, (file_no,))
        file_data = cursor.fetchone()

        cursor.close()
        connection.close()

        if file_data:
            file_content = file_data[0]
            return send_file(
                io.BytesIO(file_content),
                mimetype='application/octet-stream',  # Set the correct MIME type for EDF files
                as_attachment=True,
                download_name=f'file_{file_no}.edf'
            )
        else:
            return jsonify({"error": "File not found"}), 404

    except Exception as e:
        print("Download Error:", e)
        return jsonify({"error": "Failed to download file"}), 500


@app.route('/login_patient', methods=['POST'])
def login_patient():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        password = data['password']

        try:
            connection = create_connection()
            cursor = connection.cursor()

            sql = "SELECT * FROM patient WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                return jsonify({"message": "Login successful!"}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except pymysql.Error as e:
            return jsonify({"error": "Login failed"}), 500


@app.route('/signup', methods=['POST'])
def doctor_signup():
    if request.method == 'POST':
        data = request.get_json()

        username = data['username']
        email = data['email']
        password = data['password']

        # Check if any of the fields are empty
        if not (username and email and password):
            return jsonify({"error": "All fields must be filled"}), 400

        try:
            connection = create_connection()
            cursor = connection.cursor()

            # Check if the username already exists in the database
            sql_check_username = "SELECT * FROM patient WHERE username=%s"
            cursor.execute(sql_check_username, (username,))
            existing_username = cursor.fetchone()

            if existing_username:
                return jsonify({"error": "Username already exists"}), 409

            # Check if the email already exists in the database
            sql_check_email = "SELECT * FROM patient WHERE email=%s"
            cursor.execute(sql_check_email, (email,))
            existing_email = cursor.fetchone()

            if existing_email:
                return jsonify({"error": "Email already exists"}), 409

            # Insert the new user into the database
            sql_insert_user = "INSERT INTO patient (username, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql_insert_user, (username, email, password))
            connection.commit()

            cursor.close()
            connection.close()

            return jsonify({"message": "Patient signup successful!"}), 201

        except pymysql.Error as e:
            return jsonify({"error": "Patient signup failed"}), 500


if __name__ == "__main__":
    app.run()
