<template>
    <div class="row">
        <app-Draft v-for="draft in drafts" :key="draft.id" :draft="draft"></app-Draft>
        <router-view></router-view>
    </div>
    
</template>

<script>
import Draft from './Draft.vue';
 
export default {
    components:{
        appDraft: Draft
    },
    computed:{
        drafts(){ 
            
           return this.$store.getters.drafts;
        }
    }
}
</script>
