<template>
    <div class="col-sm-6 col-md-4">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">{{post.title}}</h5>
                <h6 class="card-subtitle mb-2 text-muted"><small>Author: {{post.author}}</small></h6>
                <p class="card-text">{{post.text}}</p>
                <!-- <router-link to="{ name: 'postdetail', params: { id: 1 }}" activeClass="active"> -->
                <a class="read_hp" @click="goTodetail">read></a>
                <!-- </router-link> -->
            </div>
        </div><br>
    </div>
</template>

<script>
export default {
    props:['post'],
    methods:{
        readPost(){
            const order = {
                postId: this.post.id,
                postAuthor :  this.post.author,
                quantity :  this.quantity

            };
            console.log(order);
        },
        goTodetail(){
            this.$store.dispatch('initPostDetail',this.post);
            this.$store.dispatch('initComments',this.post.comments);
            this.$router.push({name:'postdetail',params: { id: this.post.id }})
        }
    }
}
</script>

<style scoped>
.read_hp{
    color: rgb(44, 0, 240);
    cursor: pointer;
}
</style>

