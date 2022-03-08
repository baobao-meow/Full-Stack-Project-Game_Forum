<template>
  <!--  show before logged in, not show after logged in -->
  <div v-show = "!current_login_or_not">
      <strong>Register</strong>
      <br>
      <input type="text" v-model = "form.username_register"  placeholder="username_reg">
      <br>
      <input type="password" v-model = "form.password_register" placeholder="password_reg">
      <br>
      <input type="text" v-model="form.email_register" placeholder="Your email address">
      <button @click="send_email">Send verification code</button>
      <br>
      <input type="text" v-model="input_verification_code" placeholder="verification code">
      <button @click="check_verification_code">Check verification code</button>
      <br>
      <br>
      <!-- <div v-show="this.verification_code_correct"> -->
        <input type="button" id = "register_button" @click= "user_register" value = "register">
      <!-- </div> -->
      <br>
      <strong>{{ register_message }}</strong>
      <hr>
  </div>

</template>

<script>
// import dependencies
import axios from "axios";
export default {
  name: "register",
  // refer to https://5balloons.info/post-form-data-to-api-using-axios-in-vuejs/
  data() {
    return {
      form: {
        username_register: "",
        password_register: "",
        email_register: ""
      },
      register_message: "",
      input_verification_code: "",
      generated_verification_code: "",
      verification_code_correct: false,
      current_login_or_not: false
    }
  },
  methods: {
    user_register() {
      if(this.form.username_register == "" || this.form.password_register == ""){
        this.register_message = "Please provide valid username and password!"
      }else{
        axios
          .post('http://127.0.0.1:5000/register', this.form)
          .then(res => {
            this.register_message = res.data.message;
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    send_email(){
      if(this.form.email_register == ""){
        this.register_message = "Please provide a valid email address!";
      }else{
        axios
          .post('http://127.0.0.1:5000/send_email', {"email":this.form.email_register})
          .then(res => {
            let returned_value = res.data;
            if(returned_value['success']){
              this.generated_verification_code = returned_value['verification_code'];
              
            }else{
              console.log(returned_value)
            }
          })
          .catch(error => {
            console.log(error)
          })
      }
    },
    check_verification_code(){
      if(this.input_verification_code === this.generated_verification_code && this.generated_verification_code != ""){
          this.verification_code_correct = true;
          this.register_message = "Successfully verify email"
          console.log("successfully verify email")
      }else{
        this.register_message = "Wrong verification code, plase try again!"
      }
    }
  },
  mounted() {
      this.$bus.on('update_after_login', () => {
          this.current_login_or_not = true;
      });

      if (sessionStorage.getItem("current_login_or_not")){
         this.current_login_or_not = true;
      }
  }
}
</script>



<style scoped>
#register_button{
  background-color:chartreuse;
  font-size: 16px;
  padding: 10px 20px;
  border-radius:15px
}
</style>