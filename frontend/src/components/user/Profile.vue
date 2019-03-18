<template>
    <div class="container">
        <div id="myModel" class="row">
            <div class="col-6 col-md-4">
                <div class="box-part text-center shadow p-3 mb-5 bg-white rounded">
                     <ul>
                         <li>
                              <div class="square">
                                  <vs-button @click="popupActivo=true">
                                     <img v-bind:src="getUser.image.image_file" id="profile_img">
                                  </vs-button>
                              </div>

                            <div class="centerx">
                                <vs-popup class="holamundo"  title="Upload Your Picture" :active.sync="popupActivo">

                                    <div class="centerx">
                                        <!-- <vs-upload limit='2' fileName='image_file' action="http://127.0.0.1:8000/api/profile/6/upload_pic/" @on-success="successUpload" /> -->
                                        <!--<input type="file">
                                        <button>upload</button> -->
                                        <div class="con-input-upload"><input type="file" @change="processFile($event)"><span class="text-input">
                                            Upload File
                                            </span><span class="input-progress" style="width: 0%;"></span>
                                            <button type="button" title="Upload" class="btn-upload-all vs-upload--button-upload" @click="uploadFile">
                                                <i translate="translate" class="material-icons notranslate">
                                                cloud_upload
                                                </i>
                                            </button>

                                        </div>
                                        <div>
                                            {{getName}}
                                        </div>
                                    </div>

                                </vs-popup>
                            </div>

                         </li>
                         <li>
                             <div id='nav_myDiv'>
                                <router-link to="/profile/basic_info" tag="li"><a href="" >Basic Information</a></router-link>
                             </div>
                         </li>
                         <li>
                             <div id='nav_myDiv'>
                               <router-link to="/profile/education_work" tag="li"> <a href="">Education/Work</a> </router-link>
                             </div>
                         </li>

                     </ul>


                </div></div>
            <div class="col-12 col-md-8">
                    <router-view></router-view>
            </div>
         </div>
    </div>
</template>

<script>
import 'vue-awesome/icons/image';
export default {
    data(){
        return{
            default_image: "../src/assets/icons/profile_image.jpg",
            popupActivo:false,
            fileData : '',
        }
    },
    computed:{
        getName(){
            return this.fileData.name
        },
         getUser(){
            console.log("called")
            var user = this.$store.getters.user;
            return user;
        }
    },
    methods:{
        modelTrigger(){
            var modal = document.getElementById('myModal');
            //  $("#uploadfile").click();
              modal.style.display = "block";

        },
        successUpload(){
            this.$vs.notify({color:'success',title:'Upload Success',text:'Lorem ipsum dolor sit amet, consectetur'})
        },
        processFile(event) {
            this.fileData=''
            this.fileData = event.target.files[0]
        },
        uploadFile(){
            if(this.imageData){
                console.log(this.imageData.id)
                this.$store.dispatch('uploadFile',{'id':this.imageData.id,'image_file':this.fileData})
            }
            else{
                console.log("no image")
                this.$store.dispatch('uploadFile',{'image_file':this.fileData})
            }
        },
        getContentImageLink() {
           console.log("hello world");
        }
    },
}
</script>

<style scoped>
li{
    list-style: none
}
a{
    text-decoration: none
}
#nav_myDiv {
    width: 200px;
    margin-top: 0px;
    margin-left: 10px;
    /* border: 1px solid black; */
}
#profile_img {
    width: 100%;
    height: 100%;
    max-width: 107%;
    max-height: 130%;
    cursor: pointer;
}
img{
    max-width: 100%;
    max-height: 100%;
}
</style>

