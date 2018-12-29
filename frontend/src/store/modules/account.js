import Vue from 'vue';

const state = {
    // if the user is logged in by checking if the user has token in browser local storage
    isLoggedIn : !!localStorage.getItem('token'),
    registering : false,
    token : '',
    user : {}
};
// how the application's state changes in response to actions sent to the store
const mutations = {
    login : (state,payloads) => {
        console.log(payloads)
    },

    loginSuccess: (state,user) => {
        state.isLoggedIn = true;
        state.user = user;
        state.user.name = user.name.toUpperCase();
    },

    logout: (state)=>{
        console.log('logout')
        state.isLoggedIn=false;
        localStorage.removeItem('token');
    },

    register:(state) => {
        state.registering=true;
    }

};
//commits are payloads of information that send data from your application to your store
//way to change state in Vuex store is by commiting mutation and must be synchronized
const actions = {
    login({commit},payloads){
        return new Promise((resolve, reject) => {
            Vue.http.post('api/login/',payloads)
            .then(response =>{
                localStorage.setItem('token', response.data.token);
                const user = response.data.user;
                commit('loginSuccess', user);
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    },
    logout({commit}){
        console.log('rujal')
        localStorage.removeItem('token');
        commit('logout');
    },
    register({commit},payloads){
        console.log(payloads)
        return new Promise((resolve,reject) => {
            Vue.http.post('api/profile/',payloads)
            .then(response => {
                commit('register');
            }, error => {
                reject(error)
            })
        })
    }
}

//the way to handle side effects (like asynchronouse oprations) is by dispatching actions. 


const getters = {
    isLoggedIn: state => {
        return state.isLoggedIn
    },

    user: state =>{
        return state.user
    },
    
    registering: state => {
        return state.registering
    }
}

export default {
    state,
    actions,
    mutations,
    getters
}