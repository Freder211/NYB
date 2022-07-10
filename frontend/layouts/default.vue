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
					v-for="(section,index) in sections"
					:key="index"
					router
					:to="index"
				>
					<v-list-item-content>
						<v-list-item-title v-text="section" />
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
				<v-toolbar-title>You are currently looking at {{currentSectionName}}</v-toolbar-title>
			</v-row>

		</v-app-bar>

		<v-main>
			<Nuxt />
		</v-main>
		<v-footer padless>
			<v-col
				class="text-center"
				cols="12"
			>
				{{ new Date().getFullYear() }} • <strong>© NYB Corporate</strong>
				•
				<i>Privacy &</i> <i>Cookie policy </i>
				•
				<a
					class="link-decoration"
					href="https://github.com/Freder211/NYB"
					target="_blank"
				>Report a bug</a>
			</v-col>
		</v-footer>
	</v-app>
</template>


<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	data() {
		return {
			sections: {
				'/dashboard': 'Dashboard',
				'/communications': "Communications",
				'/schemes': "Schemes",
				'/todos': "TODO's",
				'/proscons': "Pro & Cons"
			} as unknown as string[],

			drawerOpened: true,
		};
	},

	computed: {

		currentSectionName(): string | undefined {
			const path: string = this.$route.path
			if (!path)
				return ''
			return this.sections[path]
		}

	},

	methods: {

		toggleDrawer() {
			var t = 10;
			this.drawerOpened = !this.drawerOpened;
		},

	}
})
</script>
<style>
a {
	text-decoration: none;
}
</style>
