<?php include_once("../inc/dbinfo.inc");

$id = $_GET['id'];
 
//delete contact by id
$result = mysqli_query($connection, "DELETE FROM Persons WHERE id=$id");
 
//return to home page index.php
header("Location:index.php");
?>
