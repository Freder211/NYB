<template>
	<v-container class=" mb-6">
		<v-row>
			<v-col
				cols="12"
				v-for="n in cards"
				:key="n"
			>
				<v-card
					class="mx-auto mb-6 mt-6"
					max-width="1300"
				>
					<v-row>
						<v-col cols="4">
							<v-img
								class="white--text align-end"
								height="200px"
								src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
							>
							</v-img>
						</v-col>
						<v-col cols="8">
							<v-card-title>Title of this card here</v-card-title>

							<v-card-text class="text--primary">

								<div>Scheme description, this is gonna be long. So, the thing is i have to fill this whole spaces with some text, so I'm gonna tell you my story. My name is Sam, I live in Washington DC. Back in my young ages, I used to tell stories about my life. So I'm gonna tell you my story. My name is Sam, I live in Washington DC. Back in my young ages, I used to tell stories about my life. My name is Sam, I live in Washington DC. Back in my young ages, I used to tell stories about my life. So I'm gonna tell you my story. My name is Sam, I live in Washington DC. Back in my young ages, I used to tell stories about my life.</div>
							</v-card-text>
						</v-col>
					</v-row>
					<!--
					<v-card-actions>
						<v-btn
							color="orange"
							text
						>
							Share
						</v-btn>

						<v-btn
							color="orange"
							text
						>
							Explore
						</v-btn>
					</v-card-actions>
					-->
				</v-card>
			</v-col>
		</v-row>
	</v-container>
</template>


<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
	layout: "default",

	data() {
		return {
			cards: [1, 2, 3, 4, 5, 6]

		}
	}
}
)


</script>
