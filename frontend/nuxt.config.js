export default {
	buildModules: ['@nuxt/typescript-build'],
	ssr: false,
	components: true,
	plugins: ['~plugins/filters.js'],
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
