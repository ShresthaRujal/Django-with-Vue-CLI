<template>
    <div>
        <router-view></router-view>
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
