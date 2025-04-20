<template>
  <div>
    <p>{{message}}</p>
    <input v-model="message1">
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import HelloWorld from "@/components/HelloWorld.vue"; // @ is an alias to /src

@Component({
  components: {
  }
})
export default class About extends Vue {
  
      message1='Hey retardo!';
      message2='Hey';
    


  computed: {
    somesome(): number{
        return 1;
    }
  }

}
</script>
