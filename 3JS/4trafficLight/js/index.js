
$(document).ready(function() {
    // alert('test');
    $('#stopButton').click(stop);
    $('#slowButton').click(slow);
    $('#goButton').click(go);

    function stop() {
        event.preventDefault();
        turnOff();
        //alert('test');
        $('#stopLight').css("background-color","red");
    }

    function slow() {
        event.preventDefault();
        turnOff();
        $('#slowLight').css("background-color","yellow");
    }

    function go() {
        event.preventDefault();
        turnOff();
        $('#goLight').css("background-color","green");
    }

    function turnOff() {
        $('#stopLight').css("background-color","#111");
        $('#slowLight').css("background-color","#111");
        $('#goLight').css("background-color","#111");
    }

})


