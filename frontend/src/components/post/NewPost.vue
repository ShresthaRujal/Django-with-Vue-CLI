<template>
   <div class="col-md-6">
      <h1>New Post</h1>
      <form method="POST">
         <div class="form-group">
            <label for="title">Title</label><br>
            <input type="text" name="title" class="form-control" v-model="post.title">
         </div>
         <div class="form-group">
            <label for="gener">Gener</label><br>
            <input type="text" name="gener" class="form-control" v-model="post.gener">
         </div>
         <div class="form-group">
            <label for="text">Text</label><br>
            <textarea type="text" name="text" class="form-control" v-model="post.text"></textarea>
         </div>
         <button type="button" name="button" class="btn btn-primary" @click="saveNewPost">Save</button>
      </form>
   </div>
</template>

<script>
export default {
    data(){
        return{
           post :{
            title:'',
            gener:'',
            text:'',
           }
        }
    },
    methods:{
       saveNewPost(){
          this.$store.dispatch('saveNewPost',this.post);
       }
    }
}
</script>
