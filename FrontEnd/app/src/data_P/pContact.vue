<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
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
    <div class="container">
      <h4 class="form-title">Contact Us</h4>
      <form @submit.prevent="handleSubmit" class="contact-form">
        <input placeholder="Name" id="name" v-model="name" type="text" class="input" required />
        <input placeholder="Email" id="email" v-model="email" type="email" class="input" required />
        <textarea placeholder="Message" id="message" v-model="message" class="input" required rows=6></textarea>
        <button type="submit" class="btn glass" id="submit">Submit</button>
      </form>

    </div>
  </div>
</template>
  
<script>
export default {
};
</script>
  
<style scoped>
/* Your styles here */
.navbar {
  padding: 5px 0;
  font-size: 14px;
}

.container {
  max-width: 450px;
  display: flex;
  flex-direction: column;
  border-radius: 12px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  background-color: #FFFFFFCC;
  margin-top: 8dvh;
}

.form-title {
  padding-top: 20px;
  text-align: center;
  font-size: 1.5rem;
  margin-bottom: 8px;
}

.contact-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;

}

.input {

  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 2px solid #ccc;
  border-radius: 12px;
}

#message {
  height: 150px;
  /* Adjust this value to your preference */
}

#submit {
  display: block;
  /* Ensure the button occupies full width of the container */
  margin: 0 auto;
  /* Horizontally center the button within the container */
  text-align: center;
  /* Center the content within the button */

}</style>
  