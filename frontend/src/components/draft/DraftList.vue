<template>
    <div class="box">
        <div class="container">
            <div class="row">
                <app-Draft v-for="draft in drafts" :key="draft.id" :draft="draft"></app-Draft>
            </div>
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
