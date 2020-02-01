
$('li').click(function () {
  console.log("hello");
  var buttonColor = $(this).attr('id');
  console.log(buttonColor);
  //$('.display').html(buttonText);
  if (buttonColor == "grayButton") {
    $('body').attr('class', 'gray');
  } else if (buttonColor == "whiteButton") {
    $('body').attr('class', 'white');
  } else if (buttonColor == "yellowButton") {
    $('body').attr('class', 'yellow');
  } else {
    $('body').attr('class', 'blue');
  }
});



// $('#grayButton').click(switchGray);
// $('#whiteButton').click(switchWhite);
// $('#blueButton').click(switchBlue);
// $('#yellowButton').click(switchYellow);

// function switchGray() {
//   $('body').attr('class', 'gray');
// }

// function switchWhite() {
//   $('body').attr('class', 'white');
// }

// function switchBlue() {
//   $('body').attr('class', 'blue');
// }

// function switchYellow() {
//   $('body').attr('class', 'yellow');
// }