<template>
	<div>
		<v-select 
        :options="options" 
        :placeholder="this.lbl"
        v-model="selection"></v-select>
	</div>
</template>

<script>
//import axios from 'axios'
import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css';
export default {
	name:'Dropdown',
	components:{
		vSelect
    },
    props:['lbl','fp','sp'],
	data() {
		return {
            options: ["Ben","Dan","Sven","Will"],
            selection: this.selected
		}
    },
    watch:{
        selection(val){
            this.$emit('selectionMade',val);
        }
    }
}
</script>

<style scoped>
div{
    max-width: 50%;
}
</style>