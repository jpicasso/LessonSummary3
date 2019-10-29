$(document).ready(function () {
    // alert('test');

    $('#topIcon').click(dropdown);

    function dropdown(){
        event.preventDefault();
        //alert('test');
        $('ul').addClass('slideDown');
    }


})