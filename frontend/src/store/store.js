import Vue from 'vue';
import Vuex from 'vuex';

import posts from './modules/posts';
import drafts from './modules/drafts';
import comments from './modules/comments';
import * as actions from  './actions';
import account from './modules/account';

Vue.use(Vuex);

export default new Vuex.Store({
    actions,

    modules:{
        posts,
        comments,
        account,
        drafts,
    }
});