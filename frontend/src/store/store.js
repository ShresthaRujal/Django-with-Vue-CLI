import Vue from 'vue';
import Vuex from 'vuex';

import posts from './modules/posts';
import drafts from './modules/drafts';
import comments from './modules/comments';
import * as actions from  './actions';
import account from './modules/account';
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex);

export default new Vuex.Store({
    plugins: [createPersistedState()],
    actions,

    modules:{
        posts,
        comments,
        account,
        drafts,
    }
});