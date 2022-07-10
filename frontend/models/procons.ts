import { Author } from './communications';

export class ProConList {
	id?: number;
	title?: string;
	content?: string;
	date_published?: string;
	author!: Author;
	crew?: number;
	constructor() {
		this.author = new Author();
	}
}


export class ProConItem {
	id?: number;
	crew?: number;
	tdlist_id?: number;
	content?: string;
	state?: boolean;
	date_published?: string;
	author!: Author;
}