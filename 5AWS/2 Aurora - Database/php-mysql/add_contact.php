<?php include_once("../inc/dbinfo.inc"); 
include_once("header.php");?>
<html>
<body>
<h1>Add Contact</h1>
<?php
if(isset($_POST['Submit'])) {    
    $name = $_POST['name'];
    $email = $_POST['email'];
        
    // Check the fields
    if(empty($name) || empty($email)) {                
        if(empty($name)) {
            echo "<p class='fail'>Please enter the name!</p><br/>";
        }
        
        if(empty($email)) {
            echo "<p class='fail'>Please enter the email!</p><br/>";
        }
        
        //Go back to add contact
        echo "<br/><a href='javascript:self.history.back();'>Go Back</a>";
    } else { 
        //insert the data into database
        $result = mysqli_query($connection, "INSERT INTO Persons(name,email) VALUES('$name','$email')");
        
        echo "<p class='pass'>Data added successfully.</p>";
        echo "<br/><a href='index.php'>View Contacts List</a>";
    }
}
?>
</body>
</html>
