<template>
  <div class="container">

      <app-header></app-header>
      <div class="box2">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <router-view></router-view>
            </div>
          </nav>
    </div>
    </div>
</template>

<script>
import Header from './components/Header.vue';
import DialogLoader from './components/extra/DialogLoader.vue';

export default {
  components:{
    djangoLoader:DialogLoader,
    appHeader : Header,
  },
  mounted() {
		this.$root.$dialogLoader = this.$refs.dialogLoader;
	},
  created() {
    this.$store.dispatch('initPosts');
  }
}
</script>

<style scoped>
  .box2{
    margin-top: 10px;
  }
.slide-enter-active {
  animation: slide-in 200ms ease-out forwards;
}

.slide-leave-action{
  animation: slide-out 200ms ease-out forwards;
}

@keyframes slide-in {
  from {
    transform: translateY(-30px);
    opacity: 1;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes slide-out {
  from {
    transform: translateY(0);
    opacity: 1;
  }
  to {
    transform:  translateY(-30px);
    opacity: 1;
  }
}
</style>
