<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary ">
      <div class="container-fluid">
        <a class="navbar-brand" href="/pwelcome">EEG Visualizer</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText"
          aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/pabout">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/visualize">Visualize</a>
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
                <a class="nav-link" href="/pcontact">Contact Us</a>
              </li>
            </ul>

          </div>
        </div>
      </div>
    </nav>


    <div class="about-container">
      <div class="about-content">
        <h4 class="about-title" align="center">About Us</h4>
        <div class="about-description">
          <p>
            This cutting-edge EEG Predictor app harnesses the power of Deep
            Learning technology, utilizing a meticulously trained Neural Machine
            Translation (NMT) model on an extensive dataset. The culmination of
            our research and development efforts has resulted in an astounding
            89% accuracy rate, ensuring robust and reliable predictions.
          </p>
          <p>
            The Electroencephalography (EEG) Predictor serves as an invaluable
            tool in the domain of neuroscience, facilitating the interpretation
            of brainwave patterns with remarkable precision. Whether you're a
            seasoned neuroscientist, a medical professional, or an enthusiast
            with a curious mind, our app empowers you to gain deeper insights
            into brain activity and make informed decisions.
          </p>
          <p>
            We have painstakingly fine-tuned our NMT model to discern intricate
            patterns and anomalies within EEG data, enabling real-time analysis
            and actionable predictions. The app's user-friendly interface
            provides an intuitive experience, allowing you to effortlessly
            upload EEG recordings or input real-time data for instant analysis
            and prognosis.
          </p>
        </div>
      </div>
    </div>

  </div>
</template>
  
<script>
export default {
  name: "About",
};
</script>
  
<style scoped>
.about-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 87vh;
  background-color: #f7f7f7;
}

.navbar {
  padding: 5px 0;
  font-size: 14px;
}

.about-content {
  max-width: 800px;
  padding: 20px;
  border-radius: 10px;
  background-color: white;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.about-title {
  color: #333;
  margin-bottom: 20px;
}

.about-description {
  font-size: 16px;
  line-height: 1.6;
  color: #666;
}

.about-description p {
  margin-bottom: 20px;
}
</style>
  