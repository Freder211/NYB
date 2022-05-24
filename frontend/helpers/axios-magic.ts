import axios from 'axios';

export async function getList(endpoint: string) {
	const list = await axios.get('/api/' + endpoint + '/', { baseURL: 'http://localhost' })
	console.log('%c list', 'color:#FFB86C', list);
	return list.data;
}

export async function postItem(endpoint: string, object: any) {
	const obj = await axios.post('/api/' + endpoint + '/', object)
	console.log('%c list', 'color:#FFB86C', obj);
	return obj;
}