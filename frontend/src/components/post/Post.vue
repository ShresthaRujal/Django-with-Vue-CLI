<template>
    <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">
        <div class="box-part text-center shadow p-3 mb-5 bg-white rounded">
            <div class="card-header">
				<h4 class="my-0 font-weight-normal">{{post.title}}</h4>
			</div>
            <div class="card-body ">
                <h6 class="card-subtitle mb-2 text-muted"><small>Author: {{post.author}}</small></h6>
                <p class="card-text">{{post.text}}</p>
                <router-link :to="'/posts/'+post.id" tag="li" @click.native="goTodetail" ><a class="btn btn-danger">Read</a></router-link>
                <!-- ALTERNATIVE WAY to childern route-->
                <!-- <router-link to="{ name: 'postdetail', params: { id: 1 }}" activeClass="active"> -->
                <!-- <a class="read_hp" @click="goTodetail">read>></a> -->
                <!-- </router-link> -->
              
            </div>
        </div>
    </div>

    <!-- <div class="col-lg-4 col-md-4 col-sm-4 col-xs-12">
               
		<div class="box-part text-center shadow p-3 mb-5 bg-white rounded">
                        
            <i class="fa fa-instagram fa-3x" aria-hidden="true"></i>
                        
			<div class="card-header">
				<h4 class="my-0 font-weight-normal">{{post.title}}</h4>
			</div>
                        
			<div class="card-body d-flex flex-column">
                <h1 class="card-title pricing-card-title"><small class="text-muted">{{post.author}}</small></h1>
                <p class="card-text">{{post.text}}</p>
                <router-link :to="'/posts/'+post.id" tag="li" @click.native="goTodetail" ><a class="btn btn-danger">Read More</a></router-link>
            </div>           
                        
		</div>			
	</div>	 	  -->
			    
</template>

<script>
export default {
    props:['post'],
    methods:{
        goTodetail(){
            this.$store.dispatch('initPostDetail',this.post);
            this.$store.dispatch('initComments',this.post.comments);
            //  ALTERNATIVE WAY to children route
            // this.$router.push({name:'postdetail',params: { id: this.post.id }})
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
.card-header-background{
    border: 2px solid rgb(78, 192, 87);
    border-radius: 5px;
}
.card-background{ 
    border: 2px solid #924ec09a;
    border-radius: 5px;
    border-style: outset;
}
</style>

