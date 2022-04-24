<template>
	<v-app>
		<v-navigation-drawer
			fixed
			app
			clipped
			v-model="drawerOpened"
		>
			<v-list>
				<v-list-item
					v-for="section in sections"
					:key="section.name"
					router
					:to="section.path"
				>
					<v-list-item-content>
						<v-list-item-title v-text="section.name" />
					</v-list-item-content>
				</v-list-item>
			</v-list>
		</v-navigation-drawer>
		<v-app-bar
			elevation="0"
			clipped-left
			fixed
			app
		>
			<v-app-bar-nav-icon @click="toggleDrawer" />
			<v-row class="d-flex justify-center ">
				<v-toolbar-title>Site title</v-toolbar-title>
			</v-row>

		</v-app-bar>

		<v-main>
			<Nuxt />
		</v-main>
	</v-app>
</template>


<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	data() {
		return {
			sections: [
				{
					path: "/",
					name: "Dashboard"
				},
				{
					path: "/comunications",
					name: "Comunicazioni"
				},
				{
					path: "/schemes",
					name: "Schemi"
				},
				{
					path: "/todos",
					name: "TODO's"
				},
				{
					path: "/pro-cons",
					name: "Pro & Cons"
				},
			],
			drawerOpened: true,
		};
	},

	methods: {
		toggleDrawer() {
			this.drawerOpened = !this.drawerOpened;
		},

	}
})
</script>
