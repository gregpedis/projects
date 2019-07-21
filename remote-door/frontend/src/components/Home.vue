<template>
  <div>
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h2 class="title">{{surveysTitle}}</h2>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card" v-for="survey in surveys" v-bind:key="survey.id">
          <div class="card-content">
            <p class="title">{{ survey.name}}</p>
            <p class="subtitle">{{ survey.created_at.toDateString() }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { fetchSurveys } from "@/api";
export default {
  data() {
    return {
      surveys: [],
      surveysTitle: "Check out these surveys!"
    };
  },

  beforeMount() {
    fetchSurveys().then(response => {
      this.surveys = response;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
