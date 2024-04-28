<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="/welcome">EEG Visualizer</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarText"
          aria-controls="navbarText"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/about"
                >About</a
              >
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/predict">Predict</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/visualize">Visualize</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/view">View Files</a>
            </li>
          </ul>
          <div class="d-flex">
            <span class="navbar-text"> Logged in as Doctor </span>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link ms-3" aria-current="page" href="/"
                  >Log Out</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/contact">Contact Us</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <div class="flex items-center justify-center min-h-screen">
      <div class="app-container">
        <h1 class="app-title">Brain EEG Prediction</h1>
        <p class="app-description">
          Welcome to the Brain EEG Prediction App! Upload your EEG file, and we
          will perform predictions and provide you with the results. This
          medical app is designed to assist with EEG data analysis.
        </p>
        <div class="upload-section">
          <input
            type="file"
            id="fileInput"
            class="file-input file-input-bordered w-full max-w-xs"
            @change="handleFileChange"
          />
          <button id="upload" class="btn glass" @click="handleUpload">
            Predict
          </button>
        </div>
        <div class="prediction-box">
          <pre class="prediction-content" v-if="prediction !== null">
          {{ JSON.stringify(prediction, null, 2) }}
          <button class="button-84" onclick="window.open('/report', '_blank')">View Detailed Report</button>

        </pre>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios"; // Import Axios
export default {
  data() {
    return {
      selectedFile: null,
      prediction: null,
    };
  },
  methods: {
    handleFileChange(event) {
      this.selectedFile = event.target.files[0];
    },
    async handleUpload() {
      const formData = new FormData();
      formData.append("file", this.selectedFile);
      try {
        const response = await axios.post("/predict", formData); // Use Axios to make the POST request
        const data = response.data;
        if ("prediction" in data) {
          this.prediction = data.prediction;
        } else if ("error" in data) {
          this.prediction = data.error;
        } else {
          this.prediction = "Invalid response from the server.";
        }
      } catch (error) {
        this.prediction =
          "Your report is abnormal, click button below to view the detailed report.";
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  padding: 5px 0;
  font-size: 14px;
}

/* Add your styles here */
.app-container {
  padding: 30px;
  margin-top: 18dvh;
  margin-left: 35dvh;
  margin-right: 35dvh;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.app-description {
  padding: 1dvh;
}

#nextpage {
  font-weight: 600;
  margin-left: 20px;
  padding: 10px;
  font-size: 0.9rem;
}

.app-title {
  font-size: 28px;
  color: #333;
  text-align: center;
}

.app-description {
  font-size: 16px;
  text-align: center;
}

.upload-section {
  text-align: center;
}

.upload-btn {
  font-size: 0.8rem;
  text-align: center;
}

.prediction-box {
  padding-top: 3dvh;
  text-align: center;
}

#fileInput {
  font-size: 0.8rem;
  position: relative;
  font-size: 600;
}

.prediction-content {
  font-size: 16px;
  text-align: center;
  justify-content: center;

  padding-top: 8px;
  margin-left: -100px;
  /* Your prediction content styles */
}
.prediction-content {
  /* ... */
  padding-top: 8px;
}

.btn-glass {
}

.button-84 {
  margin-top: 10px !important; /* Add !important to ensure it takes precedence */
  align-items: center;
  padding: 8px 16px; /* Reduced padding for smaller size and margin */
  background-color: initial;
  background-image: linear-gradient(#464d55, #25292e);
  border-radius: 8px;
  border-width: 0;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1), 0 3px 6px rgba(0, 0, 0, 0.05);
  box-sizing: border-box;
  color: #fff;
  cursor: pointer;
  display: inline-flex;
  flex-direction: column;
  font-family: expo-brand-demi, system-ui, -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif,
    "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  font-size: 14px;
  height: 52px;
  justify-content: center;
  line-height: 1;
  margin: 0;
  outline: none;
  overflow: hidden;
  text-align: center;
  transform: translate3d(0, 0, 0);
  transition: all 150ms;
  vertical-align: baseline;
  white-space: nowrap;
}


.button-84:hover {
  box-shadow: rgba(0, 1, 0, 0.2) 0 2px 8px;
  opacity: 0.85;
}

.button-84:active {
  outline: 0;
}

.button-84:focus {
  box-shadow: rgba(0, 0, 0, 0.5) 0 0 0 3px;
}

#upload {
  font-weight: 600;
  margin-left: 20px;
  padding: 10px;
  font-size: 0.9rem;
}
</style>
