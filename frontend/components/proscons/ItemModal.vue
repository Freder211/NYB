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
						<v-form
							ref="form"
							v-model="valid"
							lazy-validation
						>
							<v-row>
								<v-col cols="12">
									<v-text-field
										label="Content*"
										v-model="item.content"
										:rules="nameRules"
										required
									></v-text-field>
								</v-col>
								<v-col cols="12">
									<v-switch
										v-model="item.state"
										:color="`${item.state ? 'green' : 'red'}`"
										:label="`${item.state ? 'This is a good thing' : 'this is a bad thing'}`"
									></v-switch>
								</v-col>

							</v-row>

						</v-form>

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
import { ProConItem } from '~/models/procons'
export default Vue.extend({
	layout: "default",
	data() {
		return {
			showModal: false,
			valid: false,
			nameRules: [
				v => !!v || 'Name is required',
				v => (v && v.length <= 20) || 'Name must be less than 20 characters',
			]
		}
	},
	props: {
		item: { type: Object, default: () => { new ProConItem() } },
	},


	methods: {

		emitItem() {
			if (this.valid && this.$refs.form!.validate()) {
				this.showModal = false;
				this.$emit('emitItem', this.item)
			}

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