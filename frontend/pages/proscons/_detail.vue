<template>
	<v-container class="mb-6">

		<!-- section header-->
		<proscons-item-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="editItem($event)"
		></proscons-item-modal>

		<v-row :align="'start'">
			<v-col cols="6">
				<h1>Current Pro/Con list:
				</h1>
			</v-col>

			<v-col
				class="text-right"
				cols="6"
			>
				<v-btn
					class="ma-2"
					dark
				>
					<v-icon
						large
						dark
						@click="handleOpen()"
					>
						mdi-plus
					</v-icon>
				</v-btn>

			</v-col>

		</v-row>

		<v-row :align="'start'">
			<v-col cols="6">
				<v-row>
					<v-col cols="12">
						<div v-for="item in rows.filter(r=>r.state==true)">
							<v-chip
								color="green"
								class="mb-1"
								@click="invertState(item)"
								@click:close="deleteItem(item)"
								close
								close-icon="mdi-delete"
							>{{item.content}}</v-chip>
						</div>
					</v-col>
				</v-row>
			</v-col>
			<v-divider vertical></v-divider>
			<v-col cols="6">
				<v-row>
					<v-col cols="12">
						<div v-for="item in rows.filter(r=>r.state==false)">
							<v-chip
								color="red"
								class="mb-1"
								@click="invertState(item)"
								@click:close="deleteItem(item)"
								close
								close-icon="mdi-delete"
							>{{item.content}}</v-chip>
							<br>

						</div>
					</v-col>

				</v-row>
			</v-col>

		</v-row>

	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { apiCreate, apiDelete, apiEdit, getItems } from '~/helpers/axios-magic'
import { ApiBaseResponse } from '~/models/communications';
import { ProConItem, ProConList } from '~/models/procons';
export default Vue.extend({
	layout: "default",

	async asyncData({ params }) {
		const id = params.detail //param
		const apiResponse: ApiBaseResponse = await getItems('proconitems', undefined, { pclist_id: id });
		const rows = apiResponse.results!;
		return { rows }
	},

	data: () => ({
		todoid: 0,
		rows: [] as ProConItem[],
		selectedItem: new ProConItem(),
	}),



	methods: {

		async loadList() {
			const apiResponse: ApiBaseResponse = await getItems('proconitems', undefined, { pclist_id: +this.$route.params.detail });
			this.rows = apiResponse.results!;
		},


		async editItem(item: ProConItem) {
			item.id ? await apiEdit('proconitems', item) : await apiCreate('proconitems', item)
			this.loadList();

		},

		handleOpen(row?: ProConList) {
			if (row) {
				this.selectedItem = { ...row }
			}
			else {
				this.selectedItem = new ProConList();
				this.selectedItem.crew = 1;
				this.selectedItem.pclist_id = +this.$route.params.detail;
			}
			(this.$refs.modal as any)?.openModal();
		},


		invertState(item: ProConItem) {
			item.state = !item.state;
			this.editItem(item);
		},

		async deleteItem(item: ProConItem) {
			await apiDelete('proconitems', item.id!);
			this.loadList();
		},


	}




})

</script>


