$(document).ready(function () {
    //alert('test');

    //provide html option element an array of city options
    //Create an array with the following values: "NYC", "SF", "LA", "ATX", "SYD"; use the array to add values to the ```<select>``` menu by using a ```for``` loop in JavaScript (don't update the HTML to do this!)
    // Use ```$.append()``` in your iteration on the drop-down menu 
    
    var cities = ["NYC", "SF", "LA", "ATX", "SYD"];

    for (var i = 0; i < 5; i++) {
        $('#city-type').append('<option>' + cities[i] + '</option>');
    }


    //when form is submitted change background picture
    /*
    - When the user changes the input of the drop-down, update the background image based on what they selected
    - Use the ```$.attr()``` function to update html classes 
    - Get the value of user input using ```$.val()```
    - Use ```if/else if/else ``` conditionals to control the flow of your application
    - Display your pseudocode as Javascript comments
    */
   
   //sets background using pre-made classes
   function setPicture() {
       // alert('test');
       //prevents page from reloading when user clicks submit; which screws stuff up sometimes
       event.preventDefault();
       
       //declares variable city
       var city = $("#city-type").val();
       
       //if then statements
       if (city == "NYC") {
           $('body').attr('class', 'nyc');
        } else if (city == "ATX") {
            $('body').addClass('austin');
        } else if (city == "LA") {
            $('body').addClass('la');
        } else if (city == "SF" || city == "San Francisco" || city == "Bay Area") {
            $('body').addClass('sf');
        } else if (city == "SYD") {
            $('body').addClass('sydney');
        }
    }
    
    //calls setPitcture function when user submits
    //Use the ```$.change``` event handler to capture user actions
    $('form').change(setPicture);
    
    
})


/*
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

*/

