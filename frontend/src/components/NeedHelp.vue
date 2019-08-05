<template>
  <div class="wrapper">
    <b-button v-b-toggle.collapse-1 variant="primary">Need help?</b-button>
    <b-collapse id="collapse-1" class="mt-2">
      <b-list-group class="help-group">
        <b-list-group-item v-b-toggle.collapse-2 class="help-item">
          1. 블럭 당했어요
          <b-collapse id="collapse-2" class="mt-2" >
            <label for="imin">imin</label> <input name="imin" type="text" placeholder="imin"> <br>
            <label for="uname">name</label> <input name="uname" type="text" place-holder="이름"> <br>
            <label for="ustory">story</label> <input name="ustory" type="text" place-holder="상황설명"> <br>
            <button name="innocent-submit" @click="test"> send it </button>
            <input name="dt" type="hidden">
          </b-collapse>
        </b-list-group-item>
        <b-list-group-item class="help-item">2. 모의지원이 뭔가요?</b-list-group-item>
        <b-list-group-item class="help-item">3. 어떻게 참여하나요?</b-list-group-item>
      </b-list-group>
    </b-collapse>
  </div>
</template>

<script>

  import axios from 'axios'
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {
    data() {
      let msg = null;
    },
    methods: {
      test() {
        const path = `http://localhost:5000/api/random`;
        axios.get(path)
            .then(resp => {
              console.log(resp)
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
  .wrapper {
    padding-left: 20px;
  }
  
  .help-group .help-item {
    width: 30%;
  }
  
  .list-item {
  
  }
  
</style>
