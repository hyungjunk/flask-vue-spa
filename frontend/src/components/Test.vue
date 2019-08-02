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
          <form action="/send_chat" method="POST">
            <input name='user-input' type="text" placeholder="type here" v-bind:value="msg">
            <input v-on:click="send_chat" name='chat-enter' type="submit" value="확인">
          </form>
        </div>
      </div>
    </div>
  </div>
  
  
</template>

<script>
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    methods: {
      send_chat () {
        alert('your message is ')
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
    width:300px;
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
    height: 30px;
    display: flex;
    flex-direction: row;
    font-size: 20px;
  }
  
  .chat-box input[name='user-input'] {
    border: none;
    height: 100%;
  }
  
  .chat-box input:focus {
    outline: none;
  }
  
  .chat-box input[name='chat-enter'] {
    font-size: 20px;
    width:15%;
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
