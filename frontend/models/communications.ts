export class Communications {
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

export class Author {
	id?: number;
	username?: string;
	constructor() {

	}
}


export class ApiBaseResponse {
	count?: number;
	next?: string;
	previous?: string;
	results?: [] = [];
}
