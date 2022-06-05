<template>
	<v-row justify="center">
		<v-dialog
			v-model="showModal"
			persistent
			max-width="600px"
		>
			<v-card>
				<v-card-title>
					<span class="text-h5">{{item.id ? "Edit item" : "New item" }}</span>
				</v-card-title>
				<v-card-text>
					<v-container>
						<v-row>
							<v-col cols="12">
								<v-text-field
									label="Title*"
									v-model="item.title"
									required
								></v-text-field>
							</v-col>

						</v-row>
					</v-container>
					<small>*Indicates required field</small>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn
						color="blue darken-1"
						text
						@click="close()"
					>
						Close
					</v-btn>
					<v-btn
						color="blue darken-1"
						text
						@click="emitItem()"
					>
						Save
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</v-row>
</template>


<script lang="ts">
import Vue from 'vue'
import { Todolists } from '~/models/todos'
export default Vue.extend({
	layout: "default",
	data() {
		return {
			showModal: false,
		}
	},
	props: {
		item: { type: Object, default: () => { new Todolists() } },
	},

	mounted() {

		console.log('%c ', 'color:#FFB86C', 'ciao');
	},
	methods: {

		emitItem() {
			this.showModal = false;
			this.$emit('emitItem', this.item)
		},

		close() {
			this.showModal = false;
		},

		openModal() {
			this.showModal = true;
		}
	},


})
</script>