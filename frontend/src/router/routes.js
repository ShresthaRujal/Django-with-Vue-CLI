import Home from '../components/Home.vue';
import Posts from '../components/post/Posts.vue';
import Drafts from '../components/draft/Drafts.vue';
import Comment from '../components/comment/Comment.vue';
import LoginPage from '../components/LoginPage.vue';
import RegisterPage from '../components/RegisterPage.vue';
import PostList from '../components/post/PostList.vue';
import PostDetail from '../components/post/PostDetail.vue';
import DraftList from '../components/draft/DraftList.vue';
import DraftDetail from '../components/draft/DraftDetail.vue';
import NewComment from '../components/comment/NewComment.vue';
import NewPost from '../components/post/NewPost.vue';
import Profile from '../components/user/Profile.vue';


export const routes = [
    { path:'/', component:Home },
    { path:'/profile', component:Profile },
    { path:'/posts', component:Posts, children:[
        {path:'',component: PostList},
        {path:':id',component: PostDetail}
    ]},
    { path:'/comments', component:Comment },
    { path:'/login',component:LoginPage },
    { path:'/register',component:RegisterPage },
    // { path:'/postdetail/:id',component:PostDetail,name:'postdetail' },
    // { path:'/draftdetail/:id',component:DraftDetail,name:'draftdetail' },
    { path:'/addcomment',component:NewComment, name:'addcomment'},
    { path:'/new-post',component:NewPost },
    { path:'/drafts',component:Drafts, children:[
        {path:'', component:DraftList},
        {path:':id', component:DraftDetail}
    ] },

]