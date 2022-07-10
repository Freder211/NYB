	<template>
	<v-container>

		<!-- section header-->
		<proscons-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="editItem($event)"
		></proscons-modal>

		<v-data-table
			:headers="headers"
			:items="rows"
			sort-by="name"
			@dblclick:row="goToDetails"
			class="elevation-1 mx-4 mt-4"
		>

			<template v-slot:item.title="{ item }">
				<nuxt-link :to="'/proscons/' + item.id">{{ item.title }}</nuxt-link>

			</template>

			<template v-slot:item.pros_count="{ item }">
				<v-chip
					v-if="item.pros_count"
					:color="'green'"
					dark
				>
					{{ item.pros_count }}
				</v-chip>
			</template>

			<template v-slot:item.cons_count="{ item }">
				<v-chip
					v-if="item.cons_count"
					:color="'red'"
					dark
				>
					{{ item.cons_count }}
				</v-chip>
			</template>

			<template v-slot:top>
				<v-toolbar flat>
					<v-toolbar-title>PRO & Cons'</v-toolbar-title>
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
import { ProConList } from '~/models/procons';
export default Vue.extend({
	layout: "default",
	data: () => ({
		rows: [] as ProConList[],
		selectedItem: new ProConList(),
		headers: [
			{
				text: 'Author',
				sortable: true,
				align: 'center',
				value: 'author.username',
			},
			{
				text: 'Item Name',
				sortable: true,
				align: 'center',
				value: 'title',
			},
			{
				text: 'Pros',
				sortable: true,
				value: 'pros_count',
				align: 'start',
			},
			{
				text: 'Cons',
				sortable: true,
				value: 'cons_count',
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
		const apiResponse: ApiBaseResponse = await getItems('proconlists', undefined, { crew: 1 });
		const rows = apiResponse.results;
		return { rows }
	},



	methods: {
		async loadList() {
			const apiResponse: ApiBaseResponse = await getItems('proconlists', undefined, { crew: 1 });
			this.rows = apiResponse.results!;
		},


		async editItem(item: ProConList) {
			item.id ? await apiEdit('proconlists', item) : await apiCreate('proconlists', item)
			this.loadList();

		},

		handleOpen(row?: ProConList) {
			if (row) {
				this.selectedItem = { ...row }
			}
			else {
				this.selectedItem = new ProConList();
				this.selectedItem.crew = 1;
			}

			(this.$refs.modal as any)?.openModal();
		},

		async deleteItem(item: any) {
			await apiDelete('proconlists', item.id!);
			this.loadList();
		},


		handleDelete(row: ProConList) {
			this.deleteItem(row)
		},

		goToDetails(event: any, itemevent: any) {
			this.$nuxt.$router.push('/proscons/' + itemevent.item!.id)

		}


	},
})
</script>
