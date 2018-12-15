<template>
    <div class="container">
        <div class="col-md-6"></h1>
            <form method='POST'>
                <div class="form-group">
                    <label for="author">Author</label><br>
                    <input type="text" class="form-control" name="author" v-model="comment.author">
                </div>
                <div class="form-group">
                    <label for="text">Text</label><br>
                    <textarea type="text" class="form-control" name="text" v-model="comment.text"></textarea>
                </div>
                <button type="button" name="button" class="btn btn-primary" @click="addComment">Comment</button>
            </form>
        </div>        
    </div>
</template>

<script>
export default {
    data () {
        return {
            comment:{
                author: '',
                text: '',
            }            
        }
    },
    computed:{
        getPostDetail(){
            return this.$store.getters.postDetail;
        }
    },
    methods:{
        addComment(){
            console.log(this.getPostDetail.id);
            this.$store.dispatch('addComment',{'id':this.getPostDetail.id,'comment':this.comment});
        }
    }
}
</script>

