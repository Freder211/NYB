import { Author } from './communications';

export class Todolists {
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
