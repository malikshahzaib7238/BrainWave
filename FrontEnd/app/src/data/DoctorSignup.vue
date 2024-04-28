<template>

  <div class="signup-container">
    <div class="signup-content">
      <h4 class="text-center signup-heading" :style="{color: 'black'}">Create Account</h4>
      <div>
        <input type="text" v-model="signupUsername" class="input input-bordered w-full max-w-xs" placeholder="Username" />
      </div>
      <div>
        <input type="email" v-model="signupEmail" class="input input-bordered w-full max-w-xs" placeholder="Email" />
      </div>
      <div>
        <input type="password" v-model="signupPassword" class="input input-bordered w-full max-w-xs" placeholder="Password" />
      </div>
      <p v-if="signupError" class="error-message">Sign Up Failed</p>
      <div class="button-container">
        <button @click="navigateBack" class="btn btn-ghost" id="Back">Back</button>
        <button @click="handleSignup" class="btn btn-ghost" id="CreateAccount">Create Account</button>
      </div>
    </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      signupUsername: "",
      signupEmail: "",
      signupPassword: "",
      signupError: false
    };
  },
  methods: {
    async handleSignup() {
      try {
        const response = await axios.post("/signup", {
          username: this.signupUsername,
          email: this.signupEmail,
          password: this.signupPassword
        });

        const { data } = response;

        if (data.message === "Patient signup successful!") {
          this.signupError = false;
          this.$router.push("/welcome");
          this.$emit("onSignupSuccess");
        } else {
          this.signupError = true;
        }
      } catch (error) {
        console.error("Error during signup:", error);
        this.signupError = true;
      }
    },
    navigateBack() {
      this.$emit("navigateBack");
    }
  }
};
</script>

<style scoped>
.signup-container {


padding: 0px;
  margin: auto;
}

.signup-content {
  max-width: 300px;
  padding: 0px;
  background-color: #fff;
}

.signup-heading {
  margin-bottom: 18px;
}

.input {
  padding: 0 20px;
  margin: 2px 35px;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.button-container {
  padding:2px;
  display: flex;
  justify-content: center;
  margin-top: 16px auto;
}

.btn {
  font-size: 0.9rem;
  font-weight: 600;
  margin-right: 23px;
  cursor: pointer;
}
#Back{
  margin-top: 5px;
  margin-left: 20px; 
}
#CreateAccount{
  margin-top: 5px;
  margin-left: 20px; 
}
</style>
