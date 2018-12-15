<template>
<div>
    <div class="container">
         <br>{{comment.create_date}}
         <div>
            <a class="btn btn-default"><span class="glyphicon glyphicon-ok">approve</span></a>
            <a class="btn btn-default"><span class="glyphicon glyphicon-remove">remove</span></a>
         </div>
         <p>{{comment.text}}</p>
         <p><small>Commented By: {{comment.author}}</small></p>
   </div>
</div>
   
</template>
<script>
export default {
   props:['comment'],
   data(){
      return{
         create_date:'',
         text:'',
         author:''
      }
   }
}
</script>
