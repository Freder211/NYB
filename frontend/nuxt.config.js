export default {
	buildModules: ['@nuxt/typescript-build'],
	ssr: false,
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
		baseURL: 'http://localhost:8000'
	},





}
