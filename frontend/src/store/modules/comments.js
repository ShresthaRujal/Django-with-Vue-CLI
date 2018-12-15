import Vue from 'vue';

const state = {
    comments:[]
}

const mutations = {
    'setComments' (state, comments){
        state.comments =  comments;
    }
}

const actions = {
    initComments : ({commit},comments) => {
        commit('setComments', comments);
    },
    addComment :({commit, rootState}, payloads) =>{
        return new Promise((resolve, reject) => {
            Vue.http.post('api/post/'+payloads.id+'/comment/',payloads.comment)
            .then(response =>{
                //do something we dont need commit in this case
                console.log(response);
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    }
}

const getters = {
    comments : state => {
        return state.comments;
    }
};

export default {
    state,
    mutations,
    getters,
    actions
}