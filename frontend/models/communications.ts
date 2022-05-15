export class Communications {
	id?: number;
	title?: string;
	content?: string;
	date_published?: string;
	author!: Author;
	constructor() {
		this.author = new Author();
	}
}

export class Author {
	id?: number;
	username?: string;
	constructor() {

	}
}
