<template>
  <div class="hello">
    <div class="chat_list_wrap">
      <div class="header">
        Helper
      </div>
      <div class="list">
        <ul>
          <li>
            <div class="oribi-chat">
              <div class="profile">
                <!--Img-->
              </div>
              <div class="chat-wrapper">
                <div>
                  <span class="name">Oribi</span> <br>
                  <div class="mention-wrapper">
                    <span class="mention"> 뭔가 어색한데 어디가 이상한건가요 </span>
                  </div>
                </div>
              </div>
              <div class="time_td">
                <div class="check">
                  <p></p>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div class="user_chat">
              <div class="profile">
                <!--Img-->
              </div>
              <div class="chat-wrapper">
                <div>
                  <span class="name">Oribi</span> <br>
                  <div class="mention-wrapper">
                    <span class="mention"> 뭔가 어색한데 어디가 이상한건가요 </span>
                  </div>
                </div>
              </div>
              <div>
                <div class="check">
                  <p></p>
                </div>
              </div>
            </div>
          </li>
          <li>
            <div class="oribi-chat">
              <div class="profile">
                <!--Img-->
              </div>
              <div class="chat-wrapper">
                <div>
                  <span class="name">Oribi</span> <br>
                  <div class="mention-wrapper">
                    <span class="mention"> 뭔가 어색한데 어디가 이상한건가요 </span>
                  </div>
                </div>
              </div>
              <div>
                <div class="check">
                  <p></p>
                </div>
              </div>
            </div>
          </li>
        </ul>
        <div class="chat-box">
          <textarea name='user-input' type="text" placeholder="type here" :value="msg"></textarea>
          <input @click="send_chat" name='chat-enter' type="submit" value="확인">
        </div>
      </div>
    </div>
  </div>


</template>

<script>
  
  import axios from 'axios'
  
  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    methods: {
      send_chat () {
        const path = `http://localhost:5000/hello`;
        axios.get(path)
          .then(response => {
            this.msg = response.data.message;
            console.log(response);
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
</script>

<style lang="less" scoped>
  * {
    margin: 0;
    padding: 0;
  }
  
  body {
    font-size: 11px;
  }
  
  .hello {
    width: 300px;
    padding-left: 50px;
  }
  
  .oribi-chat {
    text-align: left;
    padding-left: 15px;
  }
  
  .user_chat {
    text-align: right;
    padding-right: 15px;
  }
  
  .chat_list_wrap {
    list-style: none;
  }
  
  .name {
    font-weight: bold;
  }
  
  .mention-wrapper {
    display: inline-block;
    background-color: white;
    border-radius: 30px;
  }
  
  .mention {
    padding-left: 10px;
    padding-right: 10px;
  }
  
  .chat-box {
    border: 1px solid darkgrey;
    height: 50px;
    display: flex;
    flex-direction: row;
    font-size: 20px;
    position: relative;
  }
  
  .chat-box textarea[name='user-input'] {
    border: none;
    resize: none;
    width: 80%;
    height: 100%
  }
  
  .chat-box textarea:focus {
    outline: none;
  }
  
  .chat-box input[name='chat-enter'] {
    position: relative;
    vertical-align: center;
    font-size: 20px;
    width: 15%;
  }
  
  form[name='user-chatting'] {
    width: 100%;
    position: relative;
  }
  
  .chat_list_wrap .header {
    font-size: 18px;
    padding: 15px 0;
    background: #F18C7E;
    color: white;
    text-align: center;
    font-family: "Josefin Sans", sans-serif;
  }
  
  .chat_list_wrap .search {
    background: #eee;
    padding: 5px;
  }
  
  .chat_list_wrap .search input[type="text"] {
    width: 100%;
    border-radius: 4px;
    padding: 5px 0;
    border: 0;
    text-align: center;
  }
  
  .chat_list_wrap .list ul {
    width: 100%;
    list-style: none;
    background-color: powderblue;
  }
  
  .chat_list_wrap .list ul li {
    padding-top: 10px;
    padding-bottom: 10px;
  }

</style>
