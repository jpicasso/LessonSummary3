$(document).ready(function () {
    
    //alert('test');
    
    $('form').submit(convertTemp);
    
    function convertTemp() {
        event.preventDefault();
        var cTemp = parseInt($("#celsius").val());
        var fTemp = cTemp * 1.8 + 32;
        if (fTemp <= 32) {
            $('body').css("background-color", "blue");
        } else if (fTemp > 32 && fTemp < 65) {
            $('body').css("background-color", "yellow");
        } else if (fTemp >= 65 && fTemp < 100) {
            $('body').css("background-color", "Orange");
        } else {
            $('body').css("background-color", "red");
        }
        $('#fahrenheit').text(fTemp);
    }

})