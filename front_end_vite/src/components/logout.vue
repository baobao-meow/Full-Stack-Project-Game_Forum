<template>
  <div v-show = 'current_login_or_not' >
      <input type="button" @click= "user_logout"  value = "logout" id="logout_button">
  </div>
  <strong>{{operation_message }}</strong>
  <hr>
</template>

<script>
export default {
  name: "logout",
  data() {
    return {
      current_login_or_not: false,
      operation_message: ""
    }
  },
  methods: {
    user_logout() {
      sessionStorage.clear();
      // refresh page
      location.reload();
    }
  },
  mounted() {
      this.$bus.on('update_after_login', () => {
          this.current_login_or_not = true;
      })

      if (sessionStorage.getItem("current_login_or_not")){
         this.current_login_or_not = true;

      }
  }
}
</script>

<style scoped>
#logout_button{
  background-color:crimson;
  color: wheat;
  font-size: 16px;
  padding: 10px 20px;
  border-radius:15px
}
</style>