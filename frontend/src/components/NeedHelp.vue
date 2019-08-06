<template>
  <div id="app">
    <div class="container">
<!--      <img class="start-chat" src="../assets/chat.png" alt="none" @click="show=!show">-->
      <div id="jb" class="jb" @click="roateThis"></div>
    <transition name="fade">
      <p v-if="show">hello</p>
    </transition>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        show : false
      }
    },
    methods: {
      roateThis() {
        document.getElementById('jb').style.transform = 'rotate(720deg)';
      }
    }
  }
</script>

<style>
  
  .jb {
    width: 100px;
    height: 100px;
    margin: 60px auto;
    background-color: green;
    transform: rotate(0);
    transition: all ease 1s;
  }
  /*.jb:active {*/
  /*  transform: rotate(270deg);*/
  /*}*/
  
  /*.spinning {*/
  /*  width: 100px;*/
  /*  height: 100px;*/
  /*  margin: 60px auto;*/
  /*  background-color: orange;*/
  /*  transition: all ease 1s;*/
  /*}*/
  
  /*.spinning:hover {*/
  /*  transform: rotate(270deg);*/
  /*}*/
  
  /*.jb:hover {*/
  /*  transform: rotate(270deg);*/
  /*}*/
  
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }

</style>
