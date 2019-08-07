<template>
  <div id="app">
    <div class="container">
      <!--      <img class="start-chat" src="../assets/chat.png" alt="none" @click="show=!show">-->
      <div id="jb" class="jb" @click="roateThis"></div>
<!--      <transition name="fade">-->
<!--        <p v-if="show">hello</p>-->
<!--      </transition>-->
      
      <button @click="show = !show">
        Toggle
      </button>
      <transition
        v-on:before-enter="beforeEnter"
        v-on:enter="enter"
        v-on:leave="leave"
        v-bind:css="false"
      >
        <p v-if="show">
          Demo
        </p>
      </transition>
      
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        show: false
      }
    },
    methods: {
    beforeEnter: function (el) {
      el.style.opacity = 0
    },
    enter: function (el, done) {
      Velocity(el, { opacity: 1, fontSize: '1.4em' }, { duration: 300 })
      Velocity(el, { fontSize: '1em' }, { complete: done })
    },
    leave: function (el, done) {
      Velocity(el, { translateX: '15px', rotateZ: '50deg' }, { duration: 600 })
      Velocity(el, { rotateZ: '100deg' }, { loop: 2 })
      Velocity(el, {
        rotateZ: '45deg',
        translateY: '30px',
        translateX: '30px',
        opacity: 0
      }, { complete: done })
    },
      roateThis() {
      console.log('rotate')
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
