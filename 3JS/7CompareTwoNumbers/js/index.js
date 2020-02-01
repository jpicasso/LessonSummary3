$(document).ready(function(){
    // alert('hello World!');

    var comp;

    function compare(){
        var leftNum = $('#a').val();
        var rightNum = $('#b').val();
        if (leftNum > rightNum) {
            comp = ">";
        } else if (leftNum == rightNum) {
            comp = "="
        } else {
            comp = "<"
        }
        $('#comparison').text (comp);
    }
    $('#submit').click(compare);



})