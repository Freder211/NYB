	<template>
	<v-data-table
		:headers="headers"
		:items="desserts"
		sort-by="name"
		@dblclick:row="goToDetails"
		class="elevation-1 mx-4 mt-4"
	>

		<template v-slot:item.ncons="{ item }">
			<v-chip
				:color="'red'"
				dark
			>
				{{ item.ncons }}
			</v-chip>
		</template>

		<template v-slot:item.npros="{ item }">
			<v-chip
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
				<v-spacer></v-spacer>
				<v-dialog
					v-model="dialog"
					max-width="500px"
				>
					<template v-slot:activator="{ on, attrs }">
						<v-btn
							color="primary"
							dark
							class="mb-2"
							v-bind="attrs"
							v-on="on"
						>
							New Item
						</v-btn>
					</template>
					<v-card>
						<v-card-title>
							<span class="text-h5">{{ formTitle }}</span>
						</v-card-title>

						<v-card-text>
							<v-container>
								<v-row>
									<v-col cols="12">
										<v-text-field
											v-model="editedItem.name"
											label="Todo name"
										></v-text-field>
									</v-col>

								</v-row>
							</v-container>
						</v-card-text>

						<v-card-actions>
							<v-spacer></v-spacer>
							<v-btn
								color="blue darken-1"
								text
								@click="close"
							>
								Cancel
							</v-btn>
							<v-btn
								color="blue darken-1"
								text
								@click="save"
							>
								Save
							</v-btn>
						</v-card-actions>
					</v-card>
				</v-dialog>
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
								@click="closeDelete"
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
				@click="editItem(item)"
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
			<v-btn
				color="primary"
				@click="initialize"
			>
				Reset
			</v-btn>
		</template>
	</v-data-table>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	layout: "default",
	data: () => ({
		dialog: false,
		dialogDelete: false,
		headers: [
			{
				text: 'Todo\'s Name',
				sortable: true,
				align: 'center',
				value: 'name',

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
		desserts: [],
		editedIndex: -1,
		editedItem: {
			name: '',

		},
		defaultItem: {
			name: '',

		},
	}),

	computed: {
		formTitle() {
			return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
		},
	},

	watch: {
		dialog(val) {
			val || this.close()
		},
		dialogDelete(val) {
			val || this.closeDelete()
		},
	},

	created() {
		this.initialize()
	},

	methods: {
		initialize() {
			async function fetchMovies() {
				const response = await fetch('http://localhost:8000/cat/');
				// waits until the request completes...
				console.log(response);
			};

			fetchMovies()

			this.desserts = [
				{
					id: 1,
					name: 'Frozen Yogurt',
					ncons: 4,
					npros: 999

				},
				{
					id: 2,
					name: 'Ice cream sandwich',
					ncons: 4,
					npros: 999
				},
				{
					id: 3,
					name: 'Eclair',
					ncons: 4,
					npros: 999
				},
				{
					id: 4,
					name: 'Cupcake',
					ncons: 4,
					npros: 999
				},
				{
					id: 5,
					name: 'Gingerbread',
					ncons: 4,
					npros: 999
				},
				{
					id: 6,
					name: 'Jelly bean',
					ncons: 4,
					npros: 999
				},

				{
					id: 7,
					name: 'Lollipop',
					ncons: 4,
					npros: 999
				},
				{
					id: 8,
					name: 'Honeycomb',
					ncons: 4,
					npros: 999
				},
				{
					id: 9,
					name: 'Donut',
					ncons: 4,
					npros: 999
				},
				{
					id: 10,
					name: 'KitKat',
					ncons: 4,
					npros: 999
				},
			] as any
		},

		editItem(item: any) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialog = true
		},

		deleteItem(item) {
			this.editedIndex = this.desserts.indexOf(item)
			this.editedItem = Object.assign({}, item)
			this.dialogDelete = true
		},

		deleteItemConfirm() {
			this.desserts.splice(this.editedIndex, 1)
			this.closeDelete()
		},

		close() {
			this.dialog = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
		},

		closeDelete() {
			this.dialogDelete = false
			this.$nextTick(() => {
				this.editedItem = Object.assign({}, this.defaultItem)
				this.editedIndex = -1
			})
		},

		save() {
			if (this.editedIndex > -1) {
				Object.assign(this.desserts[this.editedIndex], this.editedItem)
			} else {
				this.desserts.push(this.editedItem)
			}
			this.close()
		},

		goToDetails(event: any, { item }) {
			this.$nuxt.$router.push('/todos/' + item.id)

		}


	},
})
</script>
