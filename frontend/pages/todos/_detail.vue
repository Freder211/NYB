<template>
	<v-container class=" mb-6">

		<!-- section header-->
		<v-row :align="'start'">
			<v-col cols="6">
				<h1>Todo's -> Details page of id n° {{id}}
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

		<v-row>

			<v-col cols="6">
				<v-row
					:align="'start'"
					style="height: 150px;"
				>
					<v-col
						cols="6"
						v-for="n in cardsDone"
						:key="n.id"
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
											dark
										>
											<v-icon dark>
												mdi-wrench
											</v-icon>
										</v-btn>

										<v-btn
											class="ma-2"
											color="red"
											dark
										>
											<v-icon dark>
												mdi-minus
											</v-icon>
										</v-btn>

									</v-col>
									<v-col
										cols="6"
										align="right"
									>

										<v-icon
											large
											left
											:color="n.done ? 'green' : 'red'"
										>
											mdi-checkbox-marked-circle

										</v-icon>
										<span class="text-h6 font-weight-light">User128492</span>
									</v-col>

								</v-row>

							</v-card-title>
							<hr>
							<br>
							<v-card-text class="text-h5 font-weight-bold">
								"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quasi et modi dolorem quibusdam ex consequuntur doloremque sed repellendus natus necessitatibus?"
							</v-card-text>

							<v-card-actions>
								<v-list-item class="grow">

									<v-row justify="space-between">

										<span class="subheading"> Published 22/04/2022
										</span>
									</v-row>
								</v-list-item>
							</v-card-actions>
						</v-card>
					</v-col>
				</v-row>

			</v-col>

			<v-col cols="6">
				<v-row
					:align="'start'"
					style="height: 150px;"
				>
					<v-col
						cols="6"
						v-for="n in cardsNotDone"
						:key="n.id"
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
											dark
										>
											<v-icon dark>
												mdi-wrench
											</v-icon>
										</v-btn>

										<v-btn
											class="ma-2"
											color="red"
											dark
										>
											<v-icon dark>
												mdi-minus
											</v-icon>
										</v-btn>

									</v-col>
									<v-col
										cols="6"
										align="right"
									>

										<v-icon
											large
											left
											:color="n.done ? 'green' : 'red'"
										>

											mdi-checkbox-blank-circle-outline
										</v-icon>
										<span class="text-h6 font-weight-light">User128492</span>
									</v-col>

								</v-row>

							</v-card-title>
							<hr>
							<br>
							<v-card-text class="text-h5 font-weight-bold">
								"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quasi et modi dolorem quibusdam ex consequuntur doloremque sed repellendus natus necessitatibus?"
							</v-card-text>

							<v-card-actions>
								<v-list-item class="grow">

									<v-row justify="space-between">

										<span class="subheading"> Published 22/04/2022
										</span>
									</v-row>
								</v-list-item>
							</v-card-actions>
						</v-card>
					</v-col>
				</v-row>

			</v-col>

		</v-row>

	</v-container>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	layout: "default",

	async asyncData({ params }) {
		const id = params.detail //param

		console.log('%c ', 'color:#FFB86C', params);
		return { id }
	},

	data() {
		return {
			cardsDone: [{ id: 1, done: true }, { id: 2, done: true }, { id: 3, done: true }, { id: 4, done: true }, { id: 5, done: true }],
			groupedTodos: [],
			cardsNotDone: [{ id: 6, done: false }, { id: 7, done: false }, { id: 8, done: false }, { id: 9, done: false }, { id: 10, done: false }],

		}
	},
	methods: {



	}




})

</script>


