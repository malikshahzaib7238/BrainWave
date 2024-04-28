from flask import send_file
import numpy as np
import pandas as pd
import math
import tensorflow as tf
import mne
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from io import BytesIO
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
def preprocessEDF(file_path):
    # Read a single file and preprocess it
    edf_file = mne.io.read_raw_edf(file_path, eog=['FP1', 'FP2', 'F3', 'F4',
                                                   'C3', 'C4', 'P3', 'P4', 'O1', 'O2', 'F7', 'F8',
                                                   'T3', 'T4', 'T5', 'T6', 'PZ', 'FZ', 'CZ', 'A1', 'A2'
                                                   ], verbose='error', preload=True)
    edf_file_down_sampled = edf_file.resample(
        250, npad="auto")  # Set sampling frequency to 250 Hz
    ed = edf_file_down_sampled.to_data_frame(picks=None, index=None, scalings=None,
                                             copy=True, start=None, stop=None)  # Converting into dataframe
    Fp1_Fp7 = (ed.loc[:, 'FP1']) - (ed.loc[:, 'F7'])
    FP2_F8 = (ed.loc[:, 'FP2']) - (ed.loc[:, 'F8'])
    F7_T3 = (ed.loc[:, 'F7']) - (ed.loc[:, 'T3'])
    F8_T4 = (ed.loc[:, 'F8']) - (ed.loc[:, 'T4'])
    T3_T5 = (ed.loc[:, 'T3']) - (ed.loc[:, 'T5'])
    T4_T6 = (ed.loc[:, 'T4']) - (ed.loc[:, 'T6'])
    T5_O1 = (ed.loc[:, 'T5']) - (ed.loc[:, 'O1'])
    T6_O2 = (ed.loc[:, 'T6']) - (ed.loc[:, 'O2'])
    A1_T3 = (ed.loc[:, 'A1']) - (ed.loc[:, 'T3'])
    T4_A2 = (ed.loc[:, 'T4']) - (ed.loc[:, 'A2'])
    T3_C3 = (ed.loc[:, 'T3']) - (ed.loc[:, 'C3'])
    C4_T4 = (ed.loc[:, 'C4']) - (ed.loc[:, 'T4'])
    C3_CZ = (ed.loc[:, 'C3']) - (ed.loc[:, 'CZ'])
    CZ_C4 = (ed.loc[:, 'CZ']) - (ed.loc[:, 'C4'])
    FP1_F3 = (ed.loc[:, 'FP1']) - (ed.loc[:, 'F3'])
    FP2_F4 = (ed.loc[:, 'FP2']) - (ed.loc[:, 'F4'])
    F3_C3 = (ed.loc[:, 'F3']) - (ed.loc[:, 'C3'])
    F4_C4 = (ed.loc[:, 'F4']) - (ed.loc[:, 'C4'])
    C3_P3 = (ed.loc[:, 'C3']) - (ed.loc[:, 'P3'])
    C4_P4 = (ed.loc[:, 'C4']) - (ed.loc[:, 'P4'])
    P3_O1 = (ed.loc[:, 'P3']) - (ed.loc[:, 'O1'])
    P4_O2 = (ed.loc[:, 'P4']) - (ed.loc[:, 'O2'])
    data = {
        'Fp1_Fp7': Fp1_Fp7,
        'FP2_F8': FP2_F8,
        'F7_T3': F7_T3,
        'F8_T4': F8_T4,
        'T3_T5': T3_T5,
        'T4_T6': T4_T6,
        'T5_O1': T5_O1,
        'T6_O2': T6_O2,
        'A1_T3': A1_T3,
        'T4_A2': T4_A2,
        'T3_C3': T3_C3,
        'C4_T4': C4_T4,
        'C3_CZ': C3_CZ,
        'CZ_C4': CZ_C4,
        'FP1_F3': FP1_F3,
        'FP2_F4': FP2_F4,
        'F3_C3': F3_C3,
        'F4_C4': F4_C4,
        'C3_P3': C3_P3,
        'C4_P4': C4_P4,
        'P3_O1': P3_O1,
        'P4_O2': P4_O2
    }
    new_data_frame = pd.DataFrame(data, columns=['Fp1_Fp7', 'FP2_F8', 'F7_T3', 'F8_T4', 'T3_T5', 'T4_T6', 'T5_O1',
                                                 'T6_O2', 'A1_T3', 'T4_A2', 'T3_C3', 'C4_T4', 'C3_CZ',
                                                 'CZ_C4', 'FP1_F3', 'FP2_F4', 'F3_C3', 'F4_C4', 'C3_P3',
                                                 'C4_P4', 'P3_O1', 'P4_O2'
                                                 ])
    fs = edf_file_down_sampled.info['sfreq']
    row, col = new_data_frame.shape
    n = math.ceil(row / (15000 - int(fs * 5)))
    i = 0
    j = 15000

    for y in range(n - 1):
        if y == 0:
            example_1 = new_data_frame.iloc[0:15000, :].values
            matrix = np.expand_dims(example_1, axis=0)
        elif j < row:
            example = new_data_frame.iloc[i:j, :].values
            example = np.expand_dims(example, axis=0)
            matrix = np.vstack((matrix, example))
        else:
            example = new_data_frame.iloc[-15000:, :].values
            example = np.expand_dims(example, axis=0)
            matrix = np.vstack((matrix, example))
            break
        i = int(j - (fs * 5))
        j = int(j + 15000 - (fs * 5))
    return matrix.astype('float32')


def predictEDF(file_path):

    model = tf.keras.models.load_model(
        'C:/nmt_scalp_eeg_dataset/modelbest_loss.hdf5')

    input_data = preprocessEDF(file_path)

    input_data = np.swapaxes(input_data, 1, 2)

    predictions = model.predict(input_data)

    predictions = np.mean(predictions, axis=1)

    predictions = np.argmax(predictions)
    if predictions >= 0.5:
        predictions = 1
    else:
        predictions = 0

    return predictions

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the 'temp_files' folder exists, if not, create it
    if not os.path.exists('temp_files'):
        os.makedirs('temp_files')

    print("This function is now called")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400

    if file:
        filename = secure_filename(file.filename)
        # Save the file to the 'temp_files' directory
        file_path = os.path.join('temp_files', filename)
        file.save(file_path)
        prediction = predictEDF(file_path)
        print(prediction)
        return jsonify({'prediction': prediction})

if __name__ == "__main__":
    app.run(port=9000)