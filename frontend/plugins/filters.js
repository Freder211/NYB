import Vue from 'vue';

Vue.filter('truncate', (text, length, clamp) => {
	clamp = clamp || '...';
	var node = document.createElement('div');
	node.innerHTML = text;
	var content = node.textContent;
	return content.length > length ? content.slice(0, length) + clamp : content;
})