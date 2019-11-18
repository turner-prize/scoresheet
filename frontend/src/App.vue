<template>
  <div id="app">
    <br>
    <br>
    <h2>{{ gamesPlayed }} games played in total </h2>
    <br>
    <br>
    <form @submit="submitScores">
    <Table v-bind:tableData="tableData" :key="componentKeya"/>
    <br>
    <br>
    Add new result:
    <br>
    <br>
    <Dropdown lbl="First Place" v-on:selectionMade="updateFirstPlace" :key="componentKeyb"/>
    <br>
    <Dropdown lbl="Second Place" v-on:selectionMade="updateSecondPlace" :key="componentKeyc"/>
    <input type="submit" value="Submit" class="btn">
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Dropdown from '@/components/Dropdown.vue'
import Table from '@/components/Table.vue'
export default {
  components: {
      Dropdown, 
      Table
  },
  name: 'app',
  data(){
    return{
      tableData: [],
      gamesPlayed: "",
      w: "",
      d: "",
      b: "",
      s: "",
      fp: "",
      sp: "",
      componentKeya: 0,
      componentKeyb: 1,
      componentKeyc: 2,
    }
  },
  methods:{
    renderAll(){
      axios.get("http://localhost:3000/api/scores")
          .then(res => {
            this.gamesPlayed = res.data.map(c=>c.gameNumber).length;
            this.w = res.data.map(c=>c.Will).reduce((partial_sum, a) => partial_sum + a,0)
            this.d = res.data.map(c=>c.Dan).reduce((partial_sum, a) => partial_sum + a,0)
            this.b = res.data.map(c=>c.Ben).reduce((partial_sum, a) => partial_sum + a,0)
            this.s = res.data.map(c=>c.Sven).reduce((partial_sum, a) => partial_sum + a,0)
            this.tableData = [{name:'Will', score:this.w},{name:'Dan', score:this.d},{name:'Ben', score:this.b},{name:'Sven', score:this.s}]}
            )
          .catch(err => console.log(err));

    },
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    updateFirstPlace(x){
      this.fp = x
    },
    updateSecondPlace(x){
      this.sp = x
    },
    submitScores(){
      const p = {
        winner:this.fp,
        runnerup:this.sp
      }
      axios.post("http://localhost:3000/api/scores",p)
      this.gamesPlayed += 1
      if (this.fp == 'Will'){this.w += 3}
      if (this.fp == 'Ben'){this.b += 3}
      if (this.fp == 'Dan'){this.d += 3}
      if (this.fp == 'Sven'){this.s += 3}
      if (this.sp == 'Will'){this.w += 1}
      if (this.sp == 'Ben'){this.b += 1}
      if (this.sp == 'Dan'){this.d += 1}
      if (this.sp == 'Sven'){this.s += 1}

      this.tableData = [{name:'Will', score:this.w},{name:'Dan', score:this.d},{name:'Ben', score:this.b},{name:'Sven', score:this.s}]
      this.componentKeyb += 3;
      this.componentKeyc += 5;
      }
    },
  created() {
    this.renderAll()
  }
}

</script>

<style>
div{
  margin: 0 auto;
  text-align:center;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

input[type=submit] {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>