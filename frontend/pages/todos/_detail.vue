<template>
	<v-container class="mb-6">

		<!-- section header-->
		<todos-item-modal
			ref="modal"
			:item="selectedItem"
			@emitItem="editItem($event)"
		></todos-item-modal>

		<v-row :align="'start'">
			<v-col cols="6">
				<h1>Current todo list: {{todo.title}}
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
				<div v-for="item in rows.filter(r=>r.state==true)">
					{{item.state}}
				</div>
			</v-col>

			<v-col cols="6">
				<div v-for="item in rows.filter(r=>r.state==false)">
					{{item.state}}
				</div>
			</v-col>

		</v-row>

	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { apiCreate, apiDelete, apiEdit, getItems } from '~/helpers/axios-magic'
import { ApiBaseResponse } from '~/models/communications';
import { Todolists, TodoItems } from '~/models/todos';
export default Vue.extend({
	layout: "default",

	async asyncData({ params }) {
		const id = params.detail //param
		const apiResponse: ApiBaseResponse = await getItems('todolists', undefined, { id: id, crew: 1 });
		const todo = apiResponse!.results![0];
		return { todo }
	},

	data: () => ({
		todo: new Todolists(),
		rows: [] as TodoItems[],
		selectedItem: new TodoItems(),
	}),


	mounted() {
		this.loadList();

	},

	methods: {

		async loadList() {
			const apiResponse: ApiBaseResponse = await getItems('todoitems', undefined, { tdlist: this.todo.id, crew: 1 });
			this.rows = apiResponse.results!;
		},


		async editItem(item: TodoItems) {
			item.id ? await apiEdit('todoitems', item) : await apiCreate('todoitems', item)
			this.loadList();

		},

		handleOpen(row?: Todolists) {
			if (row) {
				this.selectedItem = { ...row }
			}
			else {
				this.selectedItem = new Todolists();
				this.selectedItem.crew = 1;
				this.selectedItem.tdlist = this.todo.id;
			}
			(this.$refs.modal as any)?.openModal();
		},


	}




})

</script>


