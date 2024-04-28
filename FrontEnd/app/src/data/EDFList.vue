<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="/welcome">EEG Visualizer</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/about">About</a>
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
            <span class="navbar-text">
              Logged in as Patient
            </span>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link ms-3" aria-current="page" href="/">Log Out</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/contact">Contact Us</a>
              </li>
            </ul>

          </div>
        </div>
      </div>
    </nav>
    <div class="edf-files-list-container">
      <div class="box">
        <div class="content">
          <h4>List of Available EDF Files</h4>
          <ul class="edf-list">
            <li v-for="(file, index) in edfFiles" :key="index" class="edf-item">
              File {{ file.No }} - <strong>Prediction: </strong>
              {{ file.Prediction === "Normal" ? "Normal" : "Abnormal" }}
              <button class="download-button" @click="generateDownloadLinks(file.No)">
                <strong>Download</strong>
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from "axios";
export default {
  data() {
    return {
      edfFiles: []
    };
  },
  mounted() {
    this.fetchEDFFiles();
  },
  methods: {
    fetchEDFFiles() {
      axios
        .get("/view")
        .then(response => {
          this.edfFiles = response.data.edf_files;
        })
        .catch(error => {
          console.error("Error fetching EDF files:", error);
        });
    },
    generateDownloadLinks(fileNo) {
      axios
        .get(`/download/${fileNo}`, { responseType: "blob" })
        .then(response => {
          const blob = new Blob([response.data], {
            type: response.headers["content-type"]
          });
          const url = URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.href = url;
          link.download = `File${fileNo}.edf`;
          link.click();
        })
        .catch(error => {
          console.error("Error generating download link:", error);
        });
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
.edf-files-list-container {
  margin-top: 10dvh;
  min-height: 10dvh;
  padding: 20px;
  margin-left: 35dvh;
  margin-right: 35dvh;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.box {

  text-align: center;
  /* Your box styles */
}

.content {
  /* Your content styles */
}

.edf-list {
  /* Your list styles */
}

.edf-item {
  /* Your item styles */
}

#head {
  font-size: 28px;
}


.navbar {
  padding: 5px 0;
  font-size: 14px;
}

.download-button {
  /* Your button styles */
}

.edf-list {
  list-style: inside;
  padding: 20px;
}

.edf-item {
  font-size: 16px;
  margin: 10px 0;
  border-bottom: 1px solid #ddd;
  padding-bottom: 10px;
}
</style>
  