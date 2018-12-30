<template>
   <div class='container'>
      <h1 class="drafttitle loader">
         {{draftDetail.title}}
      </h1>
      <div class="date draftdate">
         {{draftDetail.published_date}}
      </div>
      <div>
          <button class="btn btn-default" @click="publish">Publish</button>
         <button class="btn btn-danger">Delete</button>
      </div>
      <p class="draftcontent">{{draftDetail.text}}</p>
      <hr>
      
   </div>
</template>

<script>

export default {
    computed:{
        draftDetail(){
           console.log(this.$store.getters.draftDetail);
           return this.$store.getters.draftDetail;
        }
    },
    methods:{
        publish(){
            console.log(this.$store.getters.draftDetail.id)
            this.$store.dispatch('publish')
        }
    }
}
</script>
