import axios from 'axios';
import Cookies from 'js-cookie';
import { ApiBaseResponse } from '~/models/communications';

function buildFullEndpoint(endpoint: string, id?: number): string {
	let url = `/api/${endpoint}/`;
	id ? url += `${id}/` : '';
	return url;
}

function getCSRFtoken(): string {
	return Cookies.get('csrftoken');
}

function getNonSafeMethodAxiosConfig() {
	return {
		headers: {
			"X-CSRFtoken": getCSRFtoken()
		},
	};
}

export async function getItems(endpoint: string, itemid?: number, queryparams?: object) {
	const list = await axios.get(buildFullEndpoint(endpoint, itemid), { params: queryparams })
	return list.data;
}

export async function apiCreate(endpoint: string, payload: object): Promise<ApiBaseResponse> {
	const axiosConfig = getNonSafeMethodAxiosConfig();
	const res = await axios.post(buildFullEndpoint(endpoint), payload, axiosConfig)
	return res.data;
}


export async function apiEdit(endpoint: string, payload: any): Promise<ApiBaseResponse> {
	const axiosConfig = getNonSafeMethodAxiosConfig();
	const res = await axios.put(buildFullEndpoint(endpoint, payload.id), payload, axiosConfig)
	return res.data;
}


export async function apiDelete(endpoint: string, itemid: number): Promise<ApiBaseResponse> {
	const axiosConfig = getNonSafeMethodAxiosConfig();
	const res = await axios.delete(buildFullEndpoint(endpoint, itemid), axiosConfig)
	return res.data;
}
