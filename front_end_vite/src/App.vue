<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import axios from 'axios'
import register from "./components/register.vue";
import login from "./components/login.vue";
import display_all_post from "./components/display_all_post.vue";
import add_post from "./components/add_post.vue";
import logout from "./components/logout.vue";
import send_friend_request from "./components/send_friend_request.vue";
import notification from "./components/notification.vue";
import display_friend_list from "./components/display_friend_list.vue";
import display_shared_post_to_others from "./components/display_shared_post_to_others.vue";
import display_shared_post_to_you from "./components/display_shared_post_to_you.vue";
import chat from "./components/chat.vue";
</script>

<template>
  <div id="chat_part">
    <chat/>
  </div>
  <div id="others">
    <notification/>
    <display_shared_post_to_others/>
    <display_shared_post_to_you/>
    <display_friend_list/>
    <register/>
    <login/>
    <logout/>
    <display_all_post/>
    <add_post/>
    <send_friend_request/>
  </div>
  
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
/* #chat_part{
  float: right;
  margin-left: auto;
} */
</style>
