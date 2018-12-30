<template>
    <div class="col-sm-6 col-md-4">
        <div class="card" style="width: 18rem;">
            <div class="card-body">
                <h5 class="card-title">{{draft.title}}</h5>
                <h6 class="card-subtitle mb-2 text-muted"><small>Author: {{draft.author}}</small></h6>
                <p class="card-text">{{draft.text}}</p>
               <router-link :to="'/drafts/'+draft.id" tag="li" @click.native="goTodetail" class="btn btn-warning "><a>Open</a></router-link> 
            </div>
        </div><br>
    </div>
</template>

<script>
export default {
    props:['draft'],
    methods:{
        goTodetail(){
            console.log(this.draft)
            this.$store.dispatch('initDraftDetail',this.draft);
            // this.$router.push({name:'draftdetail',params: { id: this.draft.id }})
        }
    }
}
</script>

<style scoped>
a{
    text-decoration: none;
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    font-weight: bold;
    
}
</style>

