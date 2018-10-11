$(document).ready(function() {

	$('form').on('submit', function(event) {
		
		event.preventDefault();
		var formData = new FormData($('form')[0]);
		
		$.ajax({
			type: 'POST',
			url: '/upload',
			data: formData,
			processData : false,
			contentType: false
			success : function() {
				alert('File uploaded!');
			}
	});
});