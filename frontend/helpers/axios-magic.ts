import axios from 'axios';

export async function getList(endpoint: string) {
	const list = await axios.get('/api/' + endpoint + '/', { baseURL: 'http://localhost' })
	console.log('%c list', 'color:#FFB86C', list);
	return list.data;
}