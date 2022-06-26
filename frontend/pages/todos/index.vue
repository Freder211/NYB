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

			<template v-slot:item.title="{ item }">
				<nuxt-link :to="'/todos/' + item.id">{{ item.title }}</nuxt-link>

			</template>

			<template v-slot:item.done_count="{ item }">
				<v-chip
					v-if="item.done_count"
					:color="'green'"
					dark
				>
					{{ item.done_count }}
				</v-chip>
			</template>

			<template v-slot:item.undone_count="{ item }">
				<v-chip
					v-if="item.undone_count"
					:color="'red'"
					dark
				>
					{{ item.undone_count }}
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
					@click="handleDelete(item)"
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
				text: 'Done',
				sortable: true,
				value: 'done_count',
				align: 'start',
			},
			{
				text: 'Not done',
				sortable: true,
				value: 'undone_count',
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

		async deleteItem(item: any) {
			await apiDelete('todolists', item.id!);
			this.loadList();
		},


		handleDelete(row: Todolists) {
			this.deleteItem(row)
		},

		goToDetails(event: any, itemevent: any) {
			this.$nuxt.$router.push('/todos/' + itemevent.item!.id)

		}


	},
})
</script>
