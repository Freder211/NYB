<template>

	<v-container
		v-if="rows"
		class=" mb-6"
	>
		<!-- section header-->
		<communications-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="handleEdit($event)"
		></communications-modal>

		<v-row class="mt-2 float-right">

			<v-col cols="6">
				<v-icon
					large
					dark
					@click="handleOpen()"
				>
					mdi-plus
				</v-icon>
			</v-col>

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
						<v-row>
							<v-col cols="6">
								<v-btn
									class="ma-2"
									color="orange"
									@click="handleOpen(row)"
									dark
									small
								>
									<v-icon dark>
										mdi-wrench
									</v-icon>
								</v-btn>

								<v-btn
									class="ma-2"
									color="red"
									dark
									small
								>
									<v-icon dark>
										mdi-minus
									</v-icon>
								</v-btn>

							</v-col>
							<v-col cols="6">
								<v-icon
									large
									left
								>
									mdi-twitter
								</v-icon>
								<span class="text-h6 font-weight-light">{{row.author.username}}</span>
							</v-col>
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
import { getList, create } from '~/helpers/axios-magic'
import { ApiBaseResponse, Communications } from '../../models/communications'

export default Vue.extend({
	layout: "default",
	data() {
		return {
			rows: [] as Communications[],
			selectedItem: new Communications(),
		}
	},

	async asyncData() {
		const apiResponse: ApiBaseResponse = await getList('communications', { crew: 1 });
		const rows = apiResponse.results;
		return { rows }
	},

	methods: {
		async handleEdit(item: Communications) {
			const apiResponse = await create('communications', item);

		},

		handleOpen(row?: Communications) {
			row ? this.selectedItem = row : '';
			(this.$refs.modal as any)?.openModal();
		}
	}




})
</script>
