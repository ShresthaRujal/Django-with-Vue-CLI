<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <div class="navbar-header">
        <ul class="nav navbar-nav navbar-left">
        <router-link to="/" tag="li"><a class="navbar-brand mb-0 h1">My Blog</a></router-link>
        <router-link to="/posts" activeClass="active" tag="li"><a class="navbar-brand"><small>Posts</small></a></router-link>
        <router-link to="/support" activeClass="active" tag="li"><a class="navbar-brand"><small>Support</small></a></router-link>
        </ul>
    </div>    
  
  
  <!-- <div class="navbar-collapse">      
      <ul class="nav navbar-nav navbar-right" v-show="isLoggedIn">
          <router-link to="/new-post" activeClass="active" tag="li"><a>New Post</a></router-link>
          <router-link to="/drafts" activeClass="active" tag="li" @click.native="getDrafts"><a>Drafts</a></router-link>
          <router-link to="/login" replace activeClass="active" tag="li" @click.native="logout"><a>Log out</a></router-link>
          <router-link to="/profile" activeClass="active" tag="li"><a>Welcome: {{username}}</a></router-link>
      </ul>
  </div> -->
  <div class="nav justify-content-end" v-show="isLoggedIn">
      <ul class="nav justify-content-end">
        <li class="nav-item">
          <router-link to="/new-post" activeClass="active" tag="li"><a class="navbar-brand active" href="#"><small>New Post</small></a></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/drafts" activeClass="active" tag="li" @click.native="getDrafts"><a class="navbar-brand" href="#"><small>Drafts</small></a></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/login" replace activeClass="active" tag="li" @click.native="logout"><a class="navbar-brand" href="#"><small>Logout</small></a></router-link>
        </li>
        <li class="nav-item">
          <router-link to="/profile" replace activeClass="active" tag="li"><a class="navbar-brand" href="#"><small>Welcome: {{username}}</small></a></router-link>
        </li>
      </ul>
  </div>
  
      <ul class="navbar nav text-right" v-show="!isLoggedIn">
        <router-link to="/login" activeClass="active" tag="li"><a><v-icon name="user"/></a></router-link>     
      </ul>
  </div>
</nav>
<!-- <nav class="navbar navbar-default">
  <div class="container-fluid">
    <div class="navbar-header">
      <ul class="nav navbar-nav navbar-left">
        <router-link to="/" tag="li"><a class="navbar-brand bigbrand">My Blog</a></router-link>
        <router-link to="/posts" activeClass="active" tag="li"><a class="navbar-brand"><small>Posts</small></a></router-link>
        <router-link to="/support" activeClass="active" tag="li"><a class="navbar-brand"><small>Support</small></a></router-link>

      </ul>
      
    </div>

    <div class="collapse navbar-collapse">
      
      <ul class="nav navbar-nav navbar-right" v-show="isLoggedIn">
          <router-link to="/new-post" activeClass="active" tag="li"><a>New Post</a></router-link>
          <router-link to="/drafts" activeClass="active" tag="li" @click.native="getDrafts"><a>Drafts</a></router-link>
          <router-link to="/login" replace activeClass="active" tag="li" @click.native="logout"><a>Log out</a></router-link>
          <router-link to="/profile" activeClass="active" tag="li"><a>Welcome: {{username}}</a></router-link>
      </ul>
      <ul class="nav navbar-nav navbar-right" v-show="!isLoggedIn">
        <router-link to="/login" activeClass="active" tag="li"><a><span class="glyphicon glyphicon-user"></span></a></router-link>     
      </ul>
    </div>
  </div>
</nav> -->
</template>

<script>
import 'vue-awesome/icons/user';
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
      username(){
        var name = this.$store.getters.user.name;
        return name;
      },
      getPosts(){
          this.$store.dispatch('initPosts');
      },
      isLoggedIn(){
        return this.$store.getters.isLoggedIn;
      },
    },
    
    methods:{
      getDrafts(){
          this.$store.dispatch('initDrafts');
      },
      logout(){
        this.$store.dispatch('logout');
      }
    }
}
</script>

<style scoped>
.bigbrand{
  font-size: 1.5em;
}
</style>
