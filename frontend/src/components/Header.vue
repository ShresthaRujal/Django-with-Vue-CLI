<template>
<nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <router-link to="/" class="navbar-brand">My Blog</router-link>
    </div>

    <div class="collapse navbar-collapse">
      
      <ul class="nav navbar-nav navbar-right" v-show="isLoggedIn">
          <router-link to="/new-post" activeClass="active" tag="li"><a>New Post</a></router-link>
          <router-link to="/logout" activeClass="active" tag="li"><a @click="logout">Log out</a></router-link>
          <router-link to="/welcome" activeClass="active" tag="li"><a>Welcome: {{username}}</a></router-link>
      </ul>
      <ul class="nav navbar-nav navbar-right" v-show="!isLoggedIn">
        <router-link to="/login" activeClass="active" tag="li"><a><span class="glyphicon glyphicon-user"></span></a></router-link>     
      </ul>
    </div>
  </div>
</nav>
</template>

<script>

export default {
    data(){
      return {
        user : {
          name:'',
          email:'',
        }
      }
    },
    computed:{
      logout(){
          console.log("hello1");
       },
      username(){
        var name = this.$store.getters.user.name;
        return name;
      },
      getPosts(){
          this.$store.dispatch('initPosts');
      },
  
      isLoggedIn(){
        return this.$store.getters.isLoggedIn;
      }
    }
}
</script>
