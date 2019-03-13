import Vue from 'vue';
import { router } from '../../main.js';
// single object containing all application level state and serves as single source of truth
const state = {
    posts:[],
    post:{}
};

const mutations={
    setPost : (state,posts) => {
        state.posts = posts;
    },
    setPostDetail : (state,post) => {
        state.post = post;
    },
    saveNewPost :(state,id) =>{
        console.log(id)
        router.push('/drafts/'+id)
    }
};

const actions = {
    readPost: ({commit }, order) => {
        commit()
    },
    initPosts :({commit}) => {
        return new Promise((resolve, reject) => {
            Vue.http.get('api/post/')
            .then(response =>{
                const posts = response.data;
                commit('setPost', posts);
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    },
    initPostDetail : ({commit},post) => {
        commit('setPostDetail',post);
    },
    saveNewPost:({commit,dispatch},post) => {
        return new Promise((resolve, reject) => {
            Vue.http.post('api/post/',post)
            .then(response =>{
                dispatch('getDraft',response.data.id);
                commit('saveNewPost',response.data.id);
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    }
};

const getters = {
    posts: state => {
        console.log("post called")
        return state.posts;
    },
    postDetail : state => {
        return state.post;
    }
};

export default{
    state,
    mutations,
    actions,
    getters
}
