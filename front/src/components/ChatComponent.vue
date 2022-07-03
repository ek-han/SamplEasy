

<template>
  <div>
  <div class="form-container">
    <h1 class="signup-text">Signup to interact with fellow producers!</h1>
    <form @submit.prevent="createPost" class="form-row">
      <label class="label1" for="username">username</label>
    <input id='username' class="username" v-model="formData.username"/>
    <label class="label2" for="password">password</label>
    <input id='password' class="password" v-model="formData.password"/>
    <button class="register-button" v-on:click="gotosite('http://localhost:8000/chat')">Register </button>
    </form>
    </div>
  </div>
  </template>

<script>
import axios from "axios";



export default {
  name: "ChatComponent",

  data() {
    return{
      formData :{
        username: '',
        password: ''
      },
    }
  },
  methods:{
    createPost() {
      axios.post("http://localhost:8000/signup", this.formData)
      .then(response => console.log(response))
      .catch(error => console.log(error))
    },
    gotosite(producturl){
        window.location.href = producturl
    }
  }
};
</script>

<style scoped>

.form-container {
  position: absolute;
width: 558px;
height: 632px;
left: 680px;
top: 112px;
display: flex;
flex-direction: column;
background: #6EA6AD;
border-radius: 54px;}

.signup-text {
  position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 120px;

}


.username{
 


position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 245px;

}

.label1 {
  position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 222px;
  
}

.label2 {
  position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 320px;
}

.password {
  position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 345px;
}

.register-button {
  position: absolute;
  position: absolute;
width: 335px;
height: 50px;
left: 120px;
top: 445px;


background: #0081DF;
border-radius: 4px;
}

</style>
