<template>
	<v-container class=" mb-6">
		<!-- section header-->
		<v-row :align="'start'">
			<v-col cols="6">
			</v-col>

			<v-col
				class="text-right"
				cols="6"
			>
				<v-btn
					class="ma-2"
					dark
				>
					<v-icon>
						mdi-plus
					</v-icon>
				</v-btn>

			</v-col>

		</v-row>

		<v-row
			:align="'start'"
			style="height: 150px;"
		>
			<v-col
				cols="4"
				v-for="n in cards"
				:key="n"
			>
				<v-card
					class="mx-auto"
					dark
					max-width="400"
				>
					<v-card-title>
						<v-row
							align="right"
							justify="end"
						>
							<v-icon
								large
								left
							>
								mdi-twitter
							</v-icon>
							<span class="text-h6 font-weight-light">User128492</span>
						</v-row>

					</v-card-title>
					<hr>
					<br>
					<v-card-text class="text-h5 font-weight-bold">
						"This is a very cool project, i like cats btw.. However i don't regret having sex with unicorns"
					</v-card-text>

					<v-card-actions>
						<v-list-item class="grow">

							<v-row justify="space-between">

								<span class="subheading mr-2">
									<v-icon class="mr-1">
										mdi-heart
									</v-icon>
									256
								</span>

								<span class="subheading"> Published 22/04/2022
								</span>
							</v-row>
						</v-list-item>
					</v-card-actions>
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>
 
<script lang="ts">
import Vue from 'vue'
import axios from 'axios'
import { getList } from '../helpers/axios-magic'

export default Vue.extend({
	layout: "default",
	data() {
		return {
			cards: [1, 2, 3, 4, 5, 6]

		}
	},
	async asyncData() {
		const rows = await getList('communications')
		console.log('%c rows', 'color:#FFB86C', rows);
		return { rows }
	},




})
</script>
