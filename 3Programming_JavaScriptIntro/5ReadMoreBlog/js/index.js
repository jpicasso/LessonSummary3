$(document).ready(function(){
    // alert('hello World!');

    function expandText(){
        event.preventDefault();
        // $('#show-this-on-click').show();
        $('#show-this-on-click').slideDown();
        $('.readmore').hide();
        $('.readless').show();
    }

    function hideText(){
        event.preventDefault();
        $('#show-this-on-click').slideUp();
        $('.readmore').show();
        $('.readless').hide();
    }


    function learnText(){
        event.preventDefault();
        $('#learnmoretext').slideDown();
        $('.learnmore').hide();
    }

    $('.readmore').click(expandText);
    $('.readless').click(hideText);
    $('.learnmore').click(learnText);


})