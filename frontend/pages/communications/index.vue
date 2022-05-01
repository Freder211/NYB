<template>
	<v-container
		v-if="rows"
		class=" mb-6"
	>
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
				v-for="row in rows"
				:key="row.id"
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
							<span class="text-h6 font-weight-light">{{row.author.username}}</span>
						</v-row>

					</v-card-title>
					<hr>
					<br>
					<v-card-text class="text-h5 font-weight-bold">
						{{row.title}}

					</v-card-text>
					<v-card-text class="text-h5 font-weight-bold">
						{{row.content}}

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

								<span class="subheading"> Published {{row.date_published}}
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
import { getList } from '../../helpers/axios-magic'
import { Communications } from '../../models/communications'

export default Vue.extend({
	layout: "default",
	data() {
		return {
			rows: [] as Communications[],
			modal: false,
		}
	},
	async asyncData() {
		const rows: Communications[] = await getList('communications') as unknown as Communications[];
		console.log('%c rows', 'color:#FFB86C', rows);
		return { rows }
	},




})
</script>
