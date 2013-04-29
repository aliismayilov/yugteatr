window.onload = function() {
	var textareas = document.getElementsByTagName('textarea');

	if (textareas.length == 1) {
		CKEDITOR.replace(textareas[0].name);
	}
	else {
    	for (var i = 0; i < textareas.length - 1; i++) {
    		CKEDITOR.replace(textareas[i].name);
    	}
    }
};
