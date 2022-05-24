export default {
	buildModules: ['@nuxt/typescript-build'],
	ssr: false,
	components: true,
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
		baseURL: 'http://localhost'
	},





}
