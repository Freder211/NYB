<template>
	<v-container class="mb-6">

		<!-- section header-->
		<v-row :align="'start'">
			<v-col cols="6">
				<h1>Todo's -> Details page of id n° {{todo.title}}
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
					<v-icon>
						mdi-plus
					</v-icon>
				</v-btn>

			</v-col>

		</v-row>

	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'
import { apiCreate, apiDelete, apiEdit, getItems } from '~/helpers/axios-magic'
import { Todolists, TodoItems } from '~/models/todos';
export default Vue.extend({
	layout: "default",

	async asyncData({ params }) {
		const id = params.detail //param
		const apiResponse: ApiBaseResponse = await getItems('todolists', undefined, { id: id, crew: 1 });
		const todo = apiResponse.results[0];
		return { todo }
	},

	data: () => ({
		todo: new Todolists(),
		rows: [] as TodoItems[],
		selectedItem: new TodoItems(),
	}),

	methods: {



	}




})

</script>


