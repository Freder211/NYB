import { Author } from './communications';

export class Todolist {
	id?: number;
	title?: string;
	content?: string;
	date_published?: string;
	author!: Author;
	crew?: number;
	done_count?: number;
	undone_count?: number
	constructor() {
		this.author = new Author();
	}
}


export class TodoItem {
	id?: number;
	crew?: number;
	tdlist_id?: number;
	content?: string;
	state?: boolean;
	date_published?: string;
	author!: Author;
}