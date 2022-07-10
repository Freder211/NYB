import { Author } from './communications';

export class ProConList {
	id?: number;
	title?: string;
	content?: string;
	date_published?: string;
	author!: Author;
	crew?: number;
	pros_count?: number;
	cons_count?: number
	constructor() {
		this.author = new Author();
	}
}


export class ProConItem {
	id?: number;
	crew?: number;
	pclist_id?: number;
	content?: string;
	state?: boolean;
	date_published?: string;
	author!: Author;
}