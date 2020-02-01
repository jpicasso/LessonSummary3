$(document).ready(function(){  
    //alert("hi");
    function addListItem() {
        // get value from user input box
        // add to unordered list
        console.log('ran AddList');
        event.preventDefault();
        var newTask = $('#taskForm').val();
        // var taskList;
        // taskList.push(newTask);

        $("ul").append('<li id="1">' + newTask + '<button> remove </button> </li>');
        
    }
    
    function markDone() {
        console.log('ran markDone') 
        $(this).addClass('done');
    }
    
    function clearAll(){
        console.log('ran clearAll');
        $('ul').empty();
    }
    
    function clearCompleted() {
        console.log('ran clear completed');
        // var length = document.ul.children;
        var length = 2;
        console.log(length);
        for (i = 0; i<length; i++) {

        }

    }
    
    // function editListItem
    // show save button and hide the edit and remove buttons
    
    function removeListItem() {
        console.log('ran remove list item');
        $('#1').remove();
    }
    
    // function saveListItem
    
    $('form').submit(addListItem);
    $('#clear-btn').click(clearAll);
    $('#clearCompleted-btn').click(clearCompleted);

    //finds anchor 'ul' that is on the page...the 'li' is a dynamic part that is added later
    $('ul').on('click', 'li', markDone);
    $('ul').on('click', 'button', removeListItem);


})

