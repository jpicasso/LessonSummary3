$(document).ready(function(){
    // alert('hello World!');

    var total = 0;
    function setZero(){
        total = 0;
        $('#result').text (total);
    }
    $('#zero').click(setZero);


    function add5(){
        total = total + 5;
        $('#result').text (total);
    }
    $('#add5').click(add5);

    function add10(){
        total = total + 10;
        $('#result').text (total);
    }
    $('#add10').click(add10);

    function sub1(){
        total = total - 1;
        $('#result').text (total);
    }
    $('#sub1').click(sub1);


})