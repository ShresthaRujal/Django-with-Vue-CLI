import Vue from 'vue';
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
    saveNewPost:({commit},post) => {
        return new Promise((resolve, reject) => {
            Vue.http.post('api/post/',post)
            .then(response =>{
                resolve(response);
            }, error => {
                reject(error);
            });
       })
    }
};

const getters = {
    posts: state => {
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