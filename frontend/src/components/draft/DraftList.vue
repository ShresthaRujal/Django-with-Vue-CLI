<template>
        <div class="container">
            <div class="row">
                <p style="float: right">activities</p>
                <app-Draft v-for="draft in drafts" :key="draft.id" :draft="draft"></app-Draft>
            </div>
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

<style scoped>
</style>
