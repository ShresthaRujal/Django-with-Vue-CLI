import Vue from 'vue';
import store from '../store';
const state = {
    // all: {}
    
    userx : {}
};

const mutations = {
    uploadSuccess(state){
        console.log('update Successfull')
    },
    saveUser(state,user){
        console.log('sav')
        state.userx = user
    }
};


const actions = {
    uploadFile({commit},payload){
        return new Promise((resolve, reject) => {
            const id =store.getters.user.id
            var formData = new FormData();
            if(payload.id){
                formData.append("id",payload.id)
                formData.append("image_file",payload.image_file)
            }
            else{
                 formData.append("image_file",payload.image_file)
            }

            Vue.http.put('api/profile/'+id+'/upload_pic/',formData)
            .then(response =>{
                console.log(response)
                commit('uploadSuccess')
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    }
};

const getters = {
    userx : state => {
        return state.user;
    }
}

export default {
    state,
    actions,
    mutations,
    getters
};
