<template>
  <div class="hello">
    <b-button v-b-toggle.collapse-1 variant="primary">Need help?</b-button>
    <b-collapse id="collapse-1" class="mt-2">
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
                      <span class="mention"> 뭔가 어색한데 어디가 이상한건가요? </span>
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
    </b-collapse>
  </div>


</template>

<script>

  import axios from 'axios'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {
    name: 'HelloWorld',
    data() {
      return {
        msg: 'Welcome to Your Vue.js App',
        name: 'BootstrapVue',
        show: true
      }
    },
    watch: {
      show(newVal) {
        console.log('Alert is now ' + (newVal ? 'visible' : 'hidden'))
      }
    },
    methods: {
      send_chat() {
        const path = `http://localhost:5000/hello`
        axios.get(path)
            .then(response => {
              this.msg = response.data.message;
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })
      },
      toggle() {
        console.log('Toggle button clicked')
        this.show = !this.show
      },
      dismissed() {
        console.log('Alert dismissed')
      }
    }
  }
</script>

<style lang="less" scoped>
  * {
    margin: 0;
    padding: 0;
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
    border-radius: 15px;
    font-size: 0.8rem;
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
    height: 100%;
    font-size: 1rem;
  }
  
  .chat-box textarea:focus {
    outline: none;
  }
  
  .chat-box input[name='chat-enter'] {
    position: relative;
    vertical-align: center;
    width: 20%;
    font-size: 1rem;
  }
  
  form[name='user-chatting'] {
    width: 100%;
    position: relative;
  }
  
  .form-popup {
    display: none;
    position: fixed;
    bottom: 0;
    right: 15px;
    border: 3px solid #f1f1f1;
    z-index: 9;
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
  
  /*ssssss*/
  .form-popup {
    display: none;
    position: fixed;
    bottom: 0;
    right: 15px;
    border: 3px solid #f1f1f1;
    z-index: 9;
  }
  
  /* Add styles to the form container */
  .form-container {
    max-width: 300px;
    padding: 10px;
    background-color: white;
  }
  
  /* Full-width input fields */
  .form-container input[type=text], .form-container input[type=password] {
    width: 100%;
    padding: 15px;
    margin: 5px 0 22px 0;
    border: none;
    background: #f1f1f1;
  }
  
  /* When the inputs get focus, do something */
  .form-container input[type=text]:focus, .form-container input[type=password]:focus {
    background-color: #ddd;
    outline: none;
  }
  
  /* Set a style for the submit/login button */
  .form-container .btn {
    background-color: #4CAF50;
    color: white;
    padding: 16px 20px;
    border: none;
    cursor: pointer;
    width: 100%;
    margin-bottom: 10px;
    opacity: 0.8;
  }
  
  /* Add a red background color to the cancel button */
  .form-container .cancel {
    background-color: red;
  }
  
  /* Add some hover effects to buttons */
  .form-container .btn:hover, .open-button:hover {
    opacity: 1;
  }


</style>
