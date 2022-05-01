export default {
	buildModules: ['@nuxt/typescript-build'],
	modules: [
		'@nuxtjs/vuetify',
		'@nuxtjs/axios',
	],

	vuetify: {
		theme: {
			dark: true,
		}
	},

	axios: {
		baseURL: 'http://localohost:8000'
	}

}
