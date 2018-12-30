import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import { routes } from './router/routes';
import store from './store/store';
import VueResource from 'vue-resource';
import Icon from 'vue-awesome/components/Icon';


Vue.use(VueRouter);
Vue.use(VueResource);
Vue.component('v-icon',Icon);

Vue.http.options.root = 'http://127.0.0.1:8000/';
Vue.http.interceptors.push((request,next) => {
    var token = localStorage.getItem('token');
    if(token){
      console.log('yes header '+token)
      request.headers.set('Authorization',"Token "+token);
      localStorage.removeItem('token')
    }    
    next();
});

const router = new VueRouter({
  mode:'history',
  routes,
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
  components:{
    'v-icon':Icon
  }
})
