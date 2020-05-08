// Last Updated 2020.05.08   

$(document).ready(function () {


    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Classes
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    function Group(id, name){
        this.id = id;
        this.name = name;
    }
    function Person(id, name, picture, notes){
        this.id = id;
        this.name = name;
        this.picture = picture;
        this.notes = notes;
    }
    function PersonGroup(id, person_id, group_id){
        this.id = id;
        this.person_id = person_id;
        this.group_id = group_id;
    }

    var groups = [];
    var persons = [];
    var person_groups = [];


    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Load data from DB to local js variables
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    updateLocalVarFromDB();
    function updateLocalVarFromDB() {
        fetch('/loaddata', {
            method: 'GET',
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            var g = json.groups;
            for (i = 0; i < g.length; i++) {
                var new_group = new Group(g[i].id, g[i].name);
                groups.push(new_group);
            }
            var p = json.persons;
            for (i = 0; i < p.length; i++) {
                var new_person = new Person(p[i].id, p[i].name, p[i].picture, p[i].notes);
                persons.push(new_person);
            }
            var pg = json.person_groups;
            for (i = 0; i < pg.length; i++) {
                var new_pg = new PersonGroup(pg[i].id, pg[i].person_id, pg[i].group_id);
                person_groups.push(new_pg);
            }
            loadGroups();
            loadPersons();
            loadPerson();
        });
    }

    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Groups
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    function loadGroups() {
        for (i = 0; i < groups.length; i++) {
            var rowValue = '#tr' + groups[i].id;
            $(rowValue).remove();
        }
        for (i = 0; i < groups.length; i++) {
            $('#tableGroup').append("<tr id='tr" + groups[i].id + "'> <td id='td" + groups[i].id + "' class='span10'> " + groups[i].name + "</td> <td class='span1'> <button value = '" + groups[i].id + "'class='btn-edit'> </button> </td> <td class='span1'> <button value = '" + groups[i].id + "' class='btn-delete'> </button> </td></tr>");
        }
        for (i = 0; i < groups.length; i++) {
            $('#groups').append("<label class='CheckBoxContainer'> " + groups[i].name + "<input type='checkbox' name='categories' value='" + groups[i].id + "'> <span class='checkmark'></span></label>");
        }
    }

    function addGroup() {
        var newGroupName = prompt('Enter group name', 'Enter name here');        
        fetch('/groups', {
            method: 'POST',
            body: JSON.stringify({"name": newGroupName}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            var z = json.id;
            $('#tableGroup').append("<tr id='tr" + z + "'> <td class='span10'> " + newGroupName + "</td> <td class='span1'> <button value = '" + z + "'class='btn-edit'> </button> </td> <td class='span1'> <button value = '" + z + "' class='btn-delete'> </button> </td></tr>");
            var newGroup = new Group(z, newGroupName);
            groups.push(newGroup);
        });
    }


    function deleteGroup() {
        var group_id = $(this).val();        
        fetch('/groups/' + group_id, {
            method: 'DELETE'
        })
        for (i = 0; i < groups.length; i++) {
            if (groups[i].id == group_id) {
                var rowValue = '#tr' + group_id;
                groups.splice(group_id, 1)
                $(rowValue).remove();
            }
        }
    }            

    function editGroup() {
        var group_id = $(this).val();
        var tdValue = '#td' + group_id;
        for (i = 0; i < groups.length; i++) {
            if (groups[i].id==group_id) {
                var new_Name = prompt('Edit group name', groups[i].name);
                groups[i].name = new_Name;
                $(tdValue).html(groups[i].name);
                fetch('/groups/' + group_id, {
                    method: 'PATCH',
                    body: JSON.stringify({"name2": new_Name}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
            }
        }
    }

    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Persons
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    function loadPersons() {
        for (j = 0; j < groups.length; j++) {
            //add group table header
            var classGroup = 'table' + groups[j].name;
            var classGroupSelector = '.table' + groups[j].name;
            $('#viewGroups').append("<table class='tablePerson " + classGroup + "'><tr><th colspan=3>" + groups[j].name + " </th></tr> </table>")
            //add persons to each group
            //edit person takes you to edit person link page   
            for (i = 0; i < person_groups.length; i++) {
                var g_id = person_groups[i].group_id;
                if (groups[j].id == g_id) {
                    var p_id = person_groups[i].person_id;
                    for (k = 0; k < persons.length; k++){
                        if (persons[k].id == p_id) {
                            $(classGroupSelector).append("<tr id='tr" + i + "'> <td id='td" + i + "' class='span10'> " + persons[k].name + "</td> <td class='span1'> <button value = '" + person_groups[i].id + "'class='btn-edit'>  </button>  </td> <td class='span1'> <button value = '" + person_groups[i].id + "' class='btn-delete'> </button> </td></tr>");
                        }
                    } 
                }
            }
            //add row for adding a person
            $('#viewGroups').append("<tr id='trAdd'><td class='tableAddRow span10' colspan=2> Add Person </td> <td class='span2'> <button value= '" + groups[j].id + "' class='btn-add addPerson'> </button> <td></tr>");
        }
    }
    
    function addPerson() {
        var group_id = $(this).val();
        var newPersonName = prompt('Enter persons name', 'Enter name here');        
        var newPersonNotes = prompt('Enter persons notes', 'Enter name here');        
        var new_person_picture = "url(" + prompt('Enter persons picture', 'Please put a url link to picture')+")";

        fetch('/persons', {
            method: 'POST',
            body: JSON.stringify({"name": newPersonName, "notes": newPersonNotes, "picture": new_person_picture, "group_id": group_id}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            var p_id = json.person_id;
            var pg_id = json.person_group_id;
            var newPerson = new Person(p_id, newPersonName, newPersonPicture, newPersonNotes);
            var newPersonGroup = new PersonGroup(pg_id, p_id, group_id); 
            persons.push(newPerson);
            person_groups.push(newPersonGroup);
        });
        location.reload();
    }
          
    // takes user to view / edit person page and loads up that person
    function editPerson() {
        var person_group_id = $(this).val(); 
        var person_id = 0;
        for (i = 0; i < person_groups.length; i++){
            if (person_groups[i].id == person_group_id){
                person_id = person_groups[i].person_id;
            }
        }
        localStorage.setItem('person_id', person_id);
        window.location.href = "/edit_person";
    }

    function loadPerson() {
        var person_id = parseInt(localStorage.getItem('person_id'));
        for (i = 0; i < persons.length; i++){            
            if (persons[i].id == person_id){
                // load name, picture, notes
                $('#FaceBox-EditNotes-name').html(persons[i].name);
                $('#FaceBox-EditNotes').text(persons[i].notes);
                $('#FaceBox-EditFace').css('background-image', persons[i].picture);
                $('#FaceBox-EditFace').css('background-size', 'cover');
                $('#FaceBox-EditFace').css('background-position', 'center');
                $('#FaceBox-EditFace').css('background-repeat', 'no-repeat');
                $('#FaceBox-EditFace-p').text("");
                $('#FaceBoxText-notes').text("");
            }
        }
        loadIndividualGroups();
    }
   
    //edit persons pictures 
    function editPersonPicture() {
        //prompts user for input and then updates array
        var person_id = parseInt(localStorage.getItem('person_id'));
        var new_person_picture = '';
        for (i = 0; i < persons.length; i++){
            if (persons[i].id == person_id) {
                new_person_picture = "url(" + prompt("Add or edit full url of website", persons[i].picture)+")";
                persons[i].picture = new_person_picture;
                fetch('/persons/' + person_id, {
                    method: 'PATCH',
                    body: JSON.stringify({"picture": new_person_picture, "name": persons[i].name, "notes":persons[i].notes}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
            }
        }
        //update picture on page  
        $('#FaceBox-EditFace').css('background', new_person_picture);
        $('#FaceBox-EditFace').css('background-size', 'cover');
        $('#FaceBox-EditFace').css('background-position', 'center');
        $('#FaceBox-EditFace').css('background-repeat', 'no-repeat');
        $('#FaceBox-EditFace-p').text("");
        $('#FaceBoxText-notes').text("");
    }

    //edit persons name and then fill in the page
    function editPersonName() {
        var person_id = parseInt(localStorage.getItem('person_id'));
        var new_person_name = '';
        for (i = 0; i < persons.length; i++){
            if (persons[i].id == person_id) {
                new_person_name = prompt("Edit person's name: ", persons[i].name);
                persons[i].name = new_person_name;
                fetch('/persons/' + person_id, {
                    method: 'PATCH',
                    body: JSON.stringify({"picture": persons[i].picture, "name": new_person_name, "notes": persons[i].notes}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
            }
        }
        $('#FaceBox-EditNotes-name').html(new_person_name);
    }

    //edit persons notes and then fill in the page
    function editPersonNotes() {
        var person_id = parseInt(localStorage.getItem('person_id'));
        var new_person_notes = '';
        for (i = 0; i < persons.length; i++){
            if (persons[i].id == person_id) {
                new_person_notes = prompt("Edit person's notes: ", persons[i].notes);
                persons[i].note = new_person_notes;
                fetch('/persons/' + person_id, {
                    method: 'PATCH',
                    body: JSON.stringify({"picture": persons[i].picture, "name": persons[i].name, "notes": new_person_notes}),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
            }
        }
        $('#FaceBox-EditNotes').html(new_person_notes);
    }

    function deletePerson() {
        var confirmed = prompt('type "yes" to confirm', 'type yes here');
        if (confirmed == "yes") {   
            var person_id = parseInt(localStorage.getItem('person_id'));
            fetch('/persons/' + person_id, {
                method: 'DELETE'
            })
            for (i = 0; i < person_groups.length; i++){
                if (person_groups[i].person_id == person_id){
                    fetch('/person_groups/' + person_groups[i].id, {
                        method: 'DELETE'
                    })        
                }
            }
            window.location.href = '/persons';
        }
    }   
    
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Person_Groups
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    function deletePersonsGroup() {
        var person_group_id = $(this).val();        
        fetch('/person_groups/' + person_group_id, {
            method: 'DELETE'
        })
        location.reload();        
    }  

    function loadIndividualGroups(){
        var person_id = parseInt(localStorage.getItem('person_id'));
        for (i = 0; i < person_groups.length; i++) {
            if (person_groups[i].person_id == person_id) {
                var group_id = person_groups[i].group_id;
                for (j = 0; j < groups.length; j++) {
                    if (group_id == groups[j].id){
                        var group_name = groups[j].name;
                        $('#tableIndividualPersonsGroups').append("<tr id='tr" + group_id + "'> <td id='td" + group_id + "' class='span10'> " + group_name + "</td> <td class='span2'> <button value = '" + group_id + "' class='btn-delete'> </button> </td></tr>");
                    }
                }
            }
        }
        
        // adds group options to add group on individual page
        for (i = 0; i < groups.length; i++) {
            $('#addIndividualsGroup').append('<option value="' + groups[i].id +'">' + groups[i].name + '</option>');
        }
    }

    function addIndividualGroup() {
        var person_id = parseInt(localStorage.getItem('person_id'));
        var group_id = $(this).val();
        var new_group_name = 'whoops';
        for (i = 0; i < groups.length; i++){
            if (groups[i].id == group_id){
                new_group_name = groups[i].name;
            }
        }
        fetch('/person_groups', {
            method: 'POST',
            body: JSON.stringify({"person_id": person_id, "group_id": group_id}),
            headers: {
                'Content-Type': 'application/json'
            }
        }).then(function (response) {
            return response.json();
        }).then(function (json) {
            var new_person_group_id = json.id;
            var new_person_group = new PersonGroup(new_person_group_id, person_id, group_id);
            person_groups.push(new_person_group);
            $('#tableIndividualPersonsGroups').append("<tr id='tr" + group_id + "'> <td id='td" + group_id + "' class='span10'> " + new_group_name + "</td> <td class='span2'> <button value = '" + group_id + "' class='btn-delete'> </button> </td></tr>");
        });
    }

    function deleteIndividualGroup() {    
        var person_group_id = $(this).val();
        var person_id = parseInt(localStorage.getItem('person_id'));

        // delete person_group from table
        var rowValue = '#tr' + person_group_id;
        $(rowValue).remove();

        fetch('/person_groups/' + person_group_id, {
            method: 'DELETE'
        })
       
        // if person has no more person_groups, then add NotAssigned group
        var num_of_groups = 0;
        for (i = 0; i < person_groups.length; i++) {
            if (person_groups[i].person_id == person_id) {
                num_of_groups ++;
            } 
        }
        if (num_of_groups == 0) {
            var new_group_id = 4;
            fetch('/person_groups/', {
                method: 'POST',
                body: JSON.stringify({"person_id": person_id, "group_id": new_group_id}),
                headers: {
                    'Content-Type': 'application/json'
                }
            }).then(function (response) {
                return response.json();
            }).then(function (json) {
                var new_person_group_id = json.id;
                var new_person_group = new PersonGroup(new_person_group_id, person_id, new_group_id)
                person_groups.push(new_person_group);
            });
        }
    }    

    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Face Cards Engine
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    // temporary global variables to store names that have been selected within the group
    var card_num = 0;
    var faceOrNotes = 'notes';
    var selected_groups = [];
    var selected_pictures = [];
    var selected_names = [];
    var selected_notes = [];

    //get selected groups and load them and associate people into the selected arrays
    function getSelectedFaceGroups() {
        card_num = 0;
        selected_groups = [];
        selected_pictures = [];
        selected_names = [];
        selected_notes = [];

        //loops through each checkbox to see if selected and then adds selected check boxes to the array selected_groups
        var formFaceVar = document.forms[0];
        for (i = 0; i < formFaceVar.length; i++) {
            if (formFaceVar[i].checked) {
                selected_groups.push(formFaceVar[i].value);
            }
        }
        
        // load names, picture, and notes into selected arrays
        for (i = 0; i < selected_groups.length; i++) {
            for (j = 0; j < person_groups.length; j++) {
                if (selected_groups[i] == person_groups[j].group_id) {
                    var person_id = person_groups[j].person_id;
                    for (k = 0; k < persons.length; k++){
                        if (persons[k].id == person_id) {
                            selected_pictures.push(persons[k].picture);
                            selected_names.push(persons[k].name);
                            selected_notes.push(persons[k].notes);
                        }
                    }
                }
            }
        }
    }

     
    //Change Picture when you press next button
    function changePicture() {
        event.preventDefault();
        faceOrNotes = 'face';
        $('#FaceBox').css('background', selected_pictures[card_num]);
        $('#FaceBox').css('background-size', 'cover');
        $('#FaceBox').css('background-position', 'center');
        $('#FaceBox').css('background-repeat', 'no-repeat');
        $('#FaceBoxText').text("");
        $('#FaceBoxText-notes').text("");
    }

    function changeNote() {
        event.preventDefault();
        faceOrNotes = 'notes';
        $('#FaceBox').css('background', '');
        $('#FaceBoxText').text(selected_names[card_num]);
        $('#FaceBoxText-notes').text(selected_notes[card_num]);
        $('#FaceBox').attr('class', 'textWindow');
        for (i = 0; i < selected_names.length; i++){
        }
        if (card_num == selected_names.length - 1) {
            card_num= 0;
        } else {
            card_num = card_num +1 ;
        }
    }
    function runNextFace() {
        if (faceOrNotes == 'face') {
            return changeNote();
        } else {
            return changePicture();
        }
    }

    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    // Buttons that call functions
    // ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    // Buttons on FaceCards page
    $('#nextFace').click(runNextFace);
    $('#groups').change(getSelectedFaceGroups);

    //Buttons on FaceCardsGroups page
    $('#addGroup').click(addGroup);
    $('#tableGroup').on('click', '.btn-delete', deleteGroup);
    $('#tableGroup').on('click', '.btn-edit', editGroup);

    //buttons on FaceCardsPersons page
    $('#viewGroups').on('click', '.btn-delete', deletePersonsGroup);
    $('#viewGroups').on('click', '.btn-edit', editPerson);
    $('#viewGroups').on('click', '.addPerson', addPerson);

    //buttons on FaceCardsEditPerson page
    $('#addIndividualsGroup').change(addIndividualGroup);
    $('#tableIndividualPersonsGroups').on('click', '.btn-delete', deleteIndividualGroup);
    $('#FaceBox-EditFace').on('click', '.btn-edit', editPersonPicture);
    $('#btn-faceBox-name').click(editPersonName);
    $('#btn-faceBox-notes').click(editPersonNotes);
    $('#btn-faceBox-deletePerson').click(deletePerson);
})
