// Wait until the entire page is loaded before running this JS

$(document).ready(function(){
	//use the below to test your java script to make sure it is connected to your html; then comment it out
	//alert('hi');
	
	// Listen for a click on the element with an id of "grayButton"
	// Then, call the "switchGray" block of code
	$('#grayButton').click(switchGray);

	// Listen for a click on the element with an id of "whiteButton"
	// Then, call the "switchWhite" block of code
	$('#whiteButton').click(switchWhite);

	function switchGray(){
		// Make the body CSS background-color gray and text white
		$('body').css({
			'background-color': 'gray',
			'color': 'white'
		});
	}

	function switchWhite(){
		// Make the body CSS background-color white and text black
		$('body').css({
			'background-color': 'white',
			'color': 'black'
		});
	}
});