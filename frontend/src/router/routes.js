// import Home from '../components/Home.vue';
import Posts from '../components/post/Posts.vue';
import Comment from '../components/comment/Comment.vue';
import LoginPage from '../components/LoginPage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import PostDetail from '../components/post/PostDetail.vue';
import NewComment from '../components/comment/NewComment.vue';
import NewPost from '../components/post/NewPost.vue';

export const routes = [
    // { path:'/', component:Home },
    { path:'/', component:Posts },
    { path:'/comments', component:Comment },
    { path:'/login',component:LoginPage },
    { path:'/register',component:RegisterPage },
    { path:'/postdetail/:id',component:PostDetail,name:'postdetail' },
    { path:'/addcomment',component:NewComment, name:'addcomment'},
    { path:'/new-post',component:NewPost },

]