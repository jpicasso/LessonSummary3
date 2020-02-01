$(document).ready(function(){
    // alert('hello World!');

    var lights = 1;
    function switchLight(){
        if (lights == 1) {
            lights = 0;
            $('body').css("background-color","black");
        } else {
            lights = 1;
            $('body').css("background-color", "white");
        }
    }
    $('#light_switch').click(switchLight);



})