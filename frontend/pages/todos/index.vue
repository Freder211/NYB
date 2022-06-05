	<template>
	<v-container>

		<!-- section header-->
		<todos-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="editItem($event)"
		></todos-modal>

		<v-data-table
			:headers="headers"
			:items="rows"
			sort-by="name"
			@dblclick:row="goToDetails"
			class="elevation-1 mx-4 mt-4"
		>

			<template v-slot:item.ncons="{ item }">
				<v-chip
					v-if="item.ncons"
					:color="'red'"
					dark
				>
					{{ item.ncons }}
				</v-chip>
			</template>

			<template v-slot:item.npros="{ item }">
				<v-chip
					v-if="item.npros"
					:color="'green'"
					dark
				>
					{{ item.npros }}
				</v-chip>
			</template>

			<template v-slot:top>
				<v-toolbar flat>
					<v-toolbar-title>TODO's</v-toolbar-title>
					<v-divider
						class="mx-4"
						inset
						vertical
					></v-divider>
					<v-spacer>
						<v-icon
							large
							dark
							@click="handleOpen()"
						>
							mdi-plus
						</v-icon>
					</v-spacer>

					<v-dialog
						v-model="dialogDelete"
						max-width="500px"
					>
						<v-card>
							<v-card-title class="text-h5">Are you sure you want to delete this item?</v-card-title>
							<v-card-actions>
								<v-spacer></v-spacer>
								<v-btn
									color="blue darken-1"
									text
									@click="dialogDelete=false"
								>Cancel</v-btn>
								<v-btn
									color="blue darken-1"
									text
									@click="deleteItemConfirm"
								>OK</v-btn>
								<v-spacer></v-spacer>
							</v-card-actions>
						</v-card>
					</v-dialog>
				</v-toolbar>
			</template>
			<template v-slot:item.actions="{ item }">
				<v-icon
					small
					class="mr-2"
					@click="handleOpen(item)"
				>
					mdi-pencil
				</v-icon>
				<v-icon
					small
					@click="deleteItem(item)"
				>
					mdi-delete
				</v-icon>

			</template>
			<template v-slot:no-data>
				No data found
			</template>
		</v-data-table>
	</v-container>

</template>

<script lang="ts">
import Vue from 'vue'
import { apiCreate, apiDelete, apiEdit, getItems } from '~/helpers/axios-magic';
import { ApiBaseResponse } from '~/models/communications';
import { Todolists } from '../../models/todos'
export default Vue.extend({
	layout: "default",
	data: () => ({
		rows: [] as Todolists[],
		selectedItem: new Todolists(),
		dialogDelete: false,
		headers: [
			{
				text: 'Author',
				sortable: true,
				align: 'center',
				value: 'author.username',
			},
			{
				text: 'Todo\'s Name',
				sortable: true,
				align: 'center',
				value: 'title',
			},
			{
				text: 'N° of Pros',
				sortable: true,
				value: 'npros',
				align: 'start',
			},
			{
				text: 'N° of Cons',
				sortable: true,
				value: 'ncons',
				align: 'start',
			},
			{
				text: 'Actions',
				value: 'actions',
				sortable: false,
				align: 'center'
			},



		],
	}),

	async asyncData() {
		const apiResponse: ApiBaseResponse = await getItems('todolists', undefined, { crew: 1 });
		const rows = apiResponse.results;
		return { rows }
	},

	computed: {

	},

	watch: {
		dialogDelete(val) {
			val || false
		},
	},


	methods: {
		async loadList() {
			const apiResponse: ApiBaseResponse = await getItems('todolists', undefined, { crew: 1 });
			this.rows = apiResponse.results!;
		},


		async editItem(item: Todolists) {
			item.id ? await apiEdit('todolists', item) : await apiCreate('todolists', item)
			this.loadList();

		},

		handleOpen(row?: Todolists) {
			if (row) {
				this.selectedItem = { ...row }
			}
			else {
				this.selectedItem = new Todolists();
				this.selectedItem.crew = 1;
			}

			(this.$refs.modal as any)?.openModal();
		},

		async deleteItem(item: Todolists) {
			await apiDelete('todolists', item.id!);
			this.loadList();
		},


		deleteItemConfirm() {
			this.deleteItem(this.selectedItem)
			this.dialogDelete = false;
		},

		goToDetails(event: any, itemevent: any) {
			this.$nuxt.$router.push('/todos/' + itemevent.item!.id)

		}


	},
})
</script>
