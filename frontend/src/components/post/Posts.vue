<template>
    <div class="row">
        <app-post v-for="post in posts" :key="post.id" :post="post"></app-post>
    </div>
    
</template>

<script>
import Post from './Post.vue';
 
export default {
    components:{
        appPost: Post
    },
    computed:{
        posts(){ 
           return this.$store.getters.posts;
        }
    }
}
</script>
