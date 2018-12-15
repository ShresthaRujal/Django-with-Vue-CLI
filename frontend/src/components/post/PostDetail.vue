<template>
   <div class='container'>
      <h1 class="posttitle loader">
         {{postDetail.title}}
      </h1>
      <div class="date postdate">
         {{postDetail.published_date}}
      </div>
      <div>
         <button class="btn btn-default">Delete</button>
      </div>
      <p class="postcontent">{{postDetail.text}}</p>
      <hr>
      <router-link to="/addcomment"><a href="#" class="btn btn-primary btn-coment">AddComment</a></router-link>
      
      <app-comment v-for="comment in comments" :key="comment.id" :comment="comment"></app-comment>
   </div>
</template>

<script>
import Comment from '../comment/Comment.vue';
import NewComment from '../comment/NewComment.vue'

export default {

    data(){
        return{
           tx: this.$store.post
        }
    },
    watch:{
       '$route'(to,from){
          this.id=to.param.id;
       }
    },
    components:{
        appComment: Comment,
        appAddComment: NewComment,
    },
    computed:{
        comments(){ 
           return this.$store.getters.comments;
        },
        postDetail(){
           console.log(this.$store.getters.postDetail);
           return this.$store.getters.postDetail;
        }
    }
}
</script>
