<template>
	<v-container
		v-if="rows"
		class=" mb-6"
	>
		<!-- section header-->

		<communications-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="handleEdit()"
		></communications-modal>

		<v-row class="mt-2 float-right">
			<v-icon
				large
				dark
				@click="handleOpen()"
			>
				mdi-plus
			</v-icon>
		</v-row>
		<v-row
			align="start"
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
						<v-row justify="end">
							<v-icon
								large
								left
								@click="selectedItem=row"
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
import { getList, postItem } from '../../helpers/axios-magic'
import { apiBaseResponse, Communications } from '../../models/communications'

export default Vue.extend({
	layout: "default",
	data() {
		return {
			rows: [] as Communications[],
			openModal: false,
			selectedItem: new Communications(),
		}
	},

	async asyncData() {
		const apiResponse: apiBaseResponse = await getList('communications');
		console.log('%c rows', 'color:#FFB86C', apiResponse.results);
		const rows = apiResponse.results;
		return { rows }
	},


	methods: {
		async handleEdit() {
			console.log('%c entrato ', 'color:#FFB86C', this.$refs.modal.item.author);
			const obj = this.$refs.modal.item;
			const apiResponse = await postItem('communications', obj);
			console.log('%c rows', 'color:#FFB86C', apiResponse);

		},

		handleOpen() {
			this.$refs.modal.openModal();
		}
	}




})
</script>
