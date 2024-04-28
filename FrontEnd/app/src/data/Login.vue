<template>
  <div class="login-container">
    <div class="login-content">
      <template v-if="showSignup">
        <DoctorSignup @onSignupSuccess="setShowSignup(false)" @navigateBack="navigateBack" />
      </template>
      <template v-else>
        <h4 class="text-center" id="heading" :style="{ color: 'black' }">{{ userType === 'patient' ? 'Patient Login' :
          'Doctor Login' }}</h4>
        <div>
          <select v-model="userType" id="user-type-select" class="select select-bordered w-full max-w-xs">
            <option disabled selected>User Type</option>
            <option value="patient">Patient</option>
            <option value="doctor">Doctor</option>
          </select>
        </div>
        <template v-if="userType === 'patient'">
          <div v-if="!showSignup">
            <div>
              <input type="text" v-model="username" id="patient-username" class="input input-bordered w-full max-w-xs"
                placeholder="Username" />
            </div>
            <div>
              <input type="password" v-model="password" id="patient-password" class="input input-bordered w-full max-w-xs"
                placeholder="Password" />
            </div>
            <p v-if="loginError" class="error-message">Incorrect username or password</p> <!-- Changed loginErrorPatient to loginError -->
            <div class="button-container">
              <button @click="handleSignupClick" class="btn btn-ghost" id="SignUp">Sign Up</button>
              <button @click="handleLoginPatient" class="btn btn-ghost" id="Login">Login</button>
            </div>
          </div>
        </template>
        <template v-else-if="userType === 'doctor'">
          <div v-if="!showSignup">
            <div>
              <input type="text" v-model="username" id="doctor-username" class="input input-bordered w-full max-w-xs"
                placeholder="Doctor UserName" />
            </div>
            <div>
              <input type="password" v-model="password" id="doctor-password" class="input input-bordered w-full max-w-xs"
                placeholder="Doctor Password" />
            </div>
            <p v-if="loginError" class="error-message">Incorrect username or password</p> <!-- Keep loginError for the doctor section -->
            <div class="button-container">
              <button @click="handleLoginDoctor" class="btn btn-ghost" id="Login">Login</button>
            </div>
          </div>
        </template>
      </template>
    </div>
  </div>
</template>

<script>
import DoctorSignup from "./DoctorSignup.vue";
import axios from "axios";
export default {
  components: {
    DoctorSignup
  },
  data() {
    return {
      username: "",
      password: "",
      userType: "patient",
      loginError: false,
      showSignup: false
    };
  },
  methods: {
    async handleLoginPatient() {
      try {
        const response = await axios.post("/login_patient", {
          username: this.username,
          password: this.password
        });
        const { data } = response;

        if (data.message === "Login successful!") {
          // Login successful
          this.$router.push("/pwelcome");
          this.loginError = false;
          this.onSetUserType(this.userType);

        } else {
          this.loginError = true;
        }
      } catch (error) {
        console.error("Error during login:", error);
        this.loginError = true;
      }
    },
    async handleLoginDoctor() {
      try {
        const response = await axios.post("/login_doctor", {
          username: this.username,
          password: this.password
        });
        const { data } = response;

        if (data.message === "Login successful!") {
          // Login successful
          this.$router.push("/welcome"); // Navigate doctor to "/welcome_doc"
          this.loginError = false;
          this.onSetUserType(this.userType);
        } else {
          // Login failed
          this.loginError = true;
        }
      } catch (error) {
        console.error("Error during login:", error);
        this.loginError = true;
      }
    },
    handleSignupClick() {
      this.showSignup = true;
    },
    navigateBack() {
      this.showSignup = false;
    }
  }
};
</script>

<style scoped>
.login-container {

  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.login-content {
  max-width: 400px;
  padding: 50px;
  border: 1.5px solid #ccc;
  border-radius: 10px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Add the rest of your existing styles here */
.form-control {
  margin-bottom: 16px;
}

.center {
  margin: 0 auto;
  /* This will horizontally center the element */
  text-align: center;
  /* This will center the text inside the select element */
}

.button-container {
  display: flex;
  justify-content: center;
  margin-top: 16px;
}

#user-type-select {

  margin: 10px 5px;
  /* Center horizontally */
  padding: 8px 12px;
  /* Adjust padding to your preference */
  width: 96%;
  /* Make sure the select element takes up the available width */
  max-width: 290px;
  /* Set a maximum width for better visual control */
}



.error-message {
  color: red;
  text-align: center;
}

#SignUp {
  font-size: 0.9rem;
  font-weight: 600;
  margin-right: 23px;
}

#Login {
  font-size: 0.9rem;
  font-weight: 600;
}

#doctor-username {
  margin: 2px;
}

#doctor-password {
  margin: 2px;
}

#heading {
  margin: 12px;
}

#patient-username {
  margin: 2px;
}

#patient-password {
  margin: 2px;
}</style>
