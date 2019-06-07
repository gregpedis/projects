import Vue from 'vue';
import Router from 'vue-router';
import DoorButton from './components/DoorButton.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/doorbutton',
      name: 'DoorButton',
      component: DoorButton,
    },
    {
     path: '*',
     redirect: '/doorbutton'
    },
  ],
});
