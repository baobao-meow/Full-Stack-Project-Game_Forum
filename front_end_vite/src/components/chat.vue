<template>
<div id="chat_part">
  <strong> Chat Information </strong>
  <div v-show= "current_user">
    <div v-for="every_chat in this.all_chats">
      <div v-if="every_chat">
        <div id="each_chat">
          Users: {{ every_chat['users_in_chat'] }}
          <div v-for="each_msg in every_chat['chat_history']">
            {{ each_msg }}
          </div>
        </div>
      </div>

      <br>
      <div>
<!--        <textarea id = "send_message_content" v-model = "send_message_content" placeholder="send_message content"></textarea>-->
<!--        <input type="button" id = "send_message_button" @click= "send_chat_message()" value = "send_message">-->
      </div>
    </div>

    <div id = "start_new_chat" >
      Send to
      <select v-model = "selected_friend_to_chat">
        <option v-for = "every_friend in friend_list" :value="every_friend">{{ every_friend }}</option>
      </select>
      <br>
      <textarea id = "send_message_content" v-model = "send_message_content" placeholder="message content"></textarea>
      <br>
      <input type="button" @click= "send_chat_message()" value = "send message"/>
      <hr />
    </div>
  </div>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "chat",
  data() {
    return {
      current_user: "",
      all_chats: [],
      send_message_content: "",
      selected_friend_to_chat: "",
      friend_list: []
    }
  },
  mounted() {
    axios
        .post('http://127.0.0.1:5000/all_chats',
            {
              "current_user": sessionStorage.getItem("current_username")
            })
        .then(res => {
          this.all_chats = res.data.all_chats;
          this.operation_message = res.data.message;
          this.current_user = sessionStorage.getItem("current_username");
          this.friend_list = res.data.friend_list
          // console.log(res.data)
        })
        .catch(error => {
          console.log(error)
        });

     this.$bus.on('update_after_login', () => {
       axios
           .post('http://127.0.0.1:5000/all_chats',
               {
                 "current_user": sessionStorage.getItem("current_username")
               })
           .then(res => {
             this.all_chats = res.data.all_chats;
             this.operation_message = res.data.message;
             this.current_user = sessionStorage.getItem("current_username");
             this.friend_list = res.data.friend_list
             console.log(res.data)
           })
           .catch(error => {
             console.log(error)
           });
     })
  },
  methods: {
    send_chat_message() {
      axios
        .post('http://127.0.0.1:5000/send_chat_message',
            {
              "current_user": sessionStorage.getItem("current_username"),
              "username_send_to" : this.selected_friend_to_chat,
              "send_message_content" : this.send_message_content
            })
        .then(res => {
          location.reload()
          this.operation_message = res.data.message;
        })
        .catch(error => {
          console.log(error)
        });
    }
  }
}
</script>

<style scoped>
#each_chat{
  border-style:solid;
  border-width:2px;
  border-color:violet;
}
</style>