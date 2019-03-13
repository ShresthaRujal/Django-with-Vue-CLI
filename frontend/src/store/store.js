import Vue from 'vue';
import Vuex from 'vuex';

import posts from './modules/posts';
import drafts from './modules/drafts';
import comments from './modules/comments';
import * as actions from  './actions';
import account from './modules/account';
import users from './modules/users';
import createPersistedState from 'vuex-persistedstate';
import Vuesax from 'vuesax'; //Vuesax styles

Vue.use(Vuesax);
Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState()],
    actions,

    modules:{
        posts,
        comments,
        account,
        drafts,
        users,
    },

});
