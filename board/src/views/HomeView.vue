<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <table class="table">
      <thead>
        <tr>
          <th>uid</th>
          <th>username</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>1</td>
        </tr>
      </tbody>
      <button class="btn" > givemetheuserlisttttt</button>
    </table>

    <input type="text" :value="users" >
  </div>
</template>

<script>
import axios from 'axios'
import {reactive} from 'vue'
// import ref from 'vue'
export default {
  name: 'HomeView',
  setup(){
    let users = reactive([])

    function getUserList(){
      axios.get('http://localhost:8080/useres')
      .then((res)=> {
        users.push(res.data)
        return res.data
      }).catch(e=>{
        console.log(e);
      })
    }

    console.log(users);
    return{getUserList, users}
  }
}
</script>

<style>
table{
  width: 75%;
  margin-left: auto;
  margin-right: auto;
}

input{
  height: 300px;
  width: 500px;
}

</style>
