<template>
<div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">

  <div class="box-part text-center shadow p-3 mb-5 bg-white rounded">
            <div class="card-header">
				<h4 class="my-0 font-weight-normal">{{draft.title}}</h4>
			</div>
            <div class="card-body ">
                <h6 class="card-subtitle mb-2 text-muted"><small>Author: {{username}}</small></h6>
                <p class="card-text">{{draft.text}}</p>
                <router-link :to="'/drafts/'+draft.id" tag="li" @click.native="goTodetail" ><a class="btn btn-warning">Open</a></router-link>
                              
            </div>
        </div>
    </div>
    
</template>

<script>
export default {
    props:['draft'],
    methods:{
        goTodetail(){
            console.log(this.draft)
            this.$store.dispatch('initDraftDetail',this.draft);
        }
    },
    computed:{
        username(){
            name = this.draft.user_profile.name
            return name.charAt(0).toUpperCase() + name.slice(1)
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
li{
    list-style-type: none;
}
</style>

