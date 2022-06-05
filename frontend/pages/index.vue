<template>
	<h1>useless page</h1>
</template>
<script>
export default {
	middleware({ $auth, redirect }) {
		redirect("/dashboard")
	}

}

</script>