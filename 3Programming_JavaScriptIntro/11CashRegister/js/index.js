$(document).ready(function () {
    // alert('hello World!');

    $('#entry').submit(addValue);

    var total = 0;
    function addValue() {
        event.preventDefault();
        //alert('hello World!');
        var fieldValue = parseFloat($("#newEntry").val());
        var currency = currencyFormat(fieldValue);
        console.log(currency);
        $('#entries').append(`<tr><td colspan="2">${currency}</td></tr>`);
        total = total + fieldValue;
        $('#total').text(currencyFormat(total));
        $('#newEntry').val('');
    }
    function currencyFormat (number) {
        var newCurrency = number.toFixed(2);
        newCurrency = "$" + newCurrency;
        return newCurrency;
        //console.log(newCurrency);
    }
})