import axios from 'axios';
import Cookies from 'js-cookie';

function buildFullEndpoint(endpoint: string): string {
    return `/api/${endpoint}/`;
}

function getCSRFtoken(): string {
    return Cookies.get('csrftoken');
}

function getNonSafeMethodAxiosConfig() {
    return {
        headers: {
            "X-CSRFtoken": getCSRFtoken()
        }
    };
}

export async function getList(endpoint: string) {
	  const list = await axios.get(buildFullEndpoint(endpoint))
	console.log('%c list', 'color:#FFB86C', list);
	return list.data;
}

export async function create(endpoint: string, payload: object) {
    const axiosConfig = getNonSafeMethodAxiosConfig();
    const resp = await axios.post(buildFullEndpoint(endpoint), payload, axiosConfig)
    return resp.data;
}
