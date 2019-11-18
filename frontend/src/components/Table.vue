<template>
<div>
  <v-data-table
    :headers="headers"
    :items="this.tableData"
    :hide-default-footer="true"
    :sort-by="['score']"
    :sort-desc="['true']"
  ></v-data-table>
</div>
</template>

<script>
export default {
    name: 'Table',
    props:['tableData'],
    data() {
        return {
            headers:[
                {text: 'Player', value:'name'},
                {text: 'Points', value:'score'},
            ],
            items:[],
        }
    },
  }
</script>

<style scoped>
div{
    width: 50%;
}
</style>