<template>
	<h1>Details page of id n° {{id}}</h1>

</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	layout: "default",


	async asyncData({ params }) {
		const id = params.detail //param

		console.log('%c ', 'color:#FFB86C', params);
		return { id }
	},

})

</script>
