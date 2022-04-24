<template>
	<h1>aa</h1>
</template>
<script>
export default {
	middleware({ $auth, redirect }) {
		redirect("/dashboard")

	}
}

</script>