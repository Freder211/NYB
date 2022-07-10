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
				<v-toolbar-title>You are currently looking at {{currentSectionName}}

				</v-toolbar-title>
				<div class="avatar-icon">
					<v-menu
						bottom
						min-width="200px"
						rounded
						offset-y
					>
						<template v-slot:activator="{ on }">
							<v-btn
								icon
								x-large
								v-on="on"
							>
								<v-avatar
									color="red"
									size="48"
								>
									<span class="white--text text-h5">{{ 'xd' }}</span>
								</v-avatar>
							</v-btn>
						</template>
						<v-card>
							<v-list-item-content class="justify-center">
								<div class="mx-auto text-center">
									<v-avatar color="brown">
										<span class="white--text text-h5">{{ 'xd' }}</span>
									</v-avatar>
									<h3>{{ 'xd' }}</h3>
									<p class="text-caption mt-1">
										{{ 'xd' }}
									</p>
									<v-divider class="my-3"></v-divider>
									<v-btn
										depressed
										rounded
										text
									>
										Edit Account
									</v-btn>
									<v-divider class="my-3"></v-divider>
									<v-btn
										depressed
										rounded
										text
									>
										Disconnect
									</v-btn>
								</div>
							</v-list-item-content>
						</v-card>
					</v-menu>
				</div>

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
			for (let [key, value] of Object.entries(this.sections)) {
				if (path.includes(key)) {
					return this.sections[key]

				}

			}

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

<style scoped>
.avatar-icon {
	position: absolute;
	right: 0.3rem;
	top: 0.3rem;
}
</style>
