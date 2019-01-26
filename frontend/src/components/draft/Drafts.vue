<template>
    <div>
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
