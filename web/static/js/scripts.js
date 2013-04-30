$.fn.exists = function () {
    return this.length !== 0;
}

$(document).ready(function() {
	// toggle label
	$('#search-box').focus(function() {
		if ($('#search-box').val() == '')
			$('#search-label').hide();
	});
	$('#search-box').blur(function() {
		if ($('#search-box').val() == '')
			$('#search-label').show();
	});
	
	
	// image rotaion scripts
	if ($('#content-left img').exists()) {
		// create canvas element
		var paper = Raphael(document.getElementById('content-left'), $('#content-left').width(), $('#content-left').height() + 50);
		
		// positioning problem on IE versions less than 9
		var ieHack = 0;
		// if ($.browser.msie && parseInt($.browser.version) < 9)
		//	ieHack = -1;
		
		var marginTop = 0;
		
		// for each image in #content-left
		$('#content-left img').each(function(index) {
			// get image properties
			var width = $(this).width();
			var height = $(this).height();
			var src = $(this).attr('src');
			
			// remove image from document
			$(this).remove();
			
			// add rectangle so it will be image's border
			var border = paper.rect(8 + ieHack, 8 + ieHack + marginTop, width + 4, height + 4);
			border.rotate(-6);
			border.attr({
				fill: '#fff',
				stroke: 'none'
			});
			
			// add image and rotate
			var img = paper.image(src, 10, 10 + marginTop, width, height);
			img.rotate(-6);
			
			// increase marginTop
			marginTop += height + 10;
		});
		
		// webkit forcing
		paper.safari();
	}
	// if no image, hide this div
	else {
		$('#content-left').hide();
	}
});
