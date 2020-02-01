//delays code from executing until all DOM assets have been loaded
$(document).ready(function(){
    // alert('hello World!');

    //sets background using pre-made classes
    function setPicture(){
        //declares variable city
        var city = $("#city-type").val();
        
        //prevents page from reloading when user clicks submit; which screws stuff up sometimes
        event.preventDefault();

        //if then statements
        if (city == "NYC") {
            $('body').attr('class', 'nyc');
        } else if (city == "Austin") {
            $('body').addClass('austin');
        } else if (city == "LA" || city == "Los Angeles" || city == "LAX") {
            $('body').addClass('la');
        } else if (city == "SF" || city == "San Francisco" || city == "Bay Area") {
            $('body').addClass('sf');
        } else if (city == "Sydney" || city == "SYD") {
            $('body').addClass('sydney');
        } else {
            //catch all if user doesn't enter one of the above
            alert("City not recognized or we don't have it");
        }
    }

    //calls setPitcture function when user submits
    $('form').submit(setPicture);
})