import Vue from 'vue';

export const loadData = ({commit}) => {
    Vue.http.get('data.json')
    .then(Response => response.json())
    .then(data => {
        if (data) {
            const posts = data.posts; 
            commit('SET_POSTS',posts);
        }
    });
}