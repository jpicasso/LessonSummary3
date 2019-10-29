<?php include_once("../inc/dbinfo.inc");
include_once("header.php"); 
 ?>
<html>
<body>
<h1>Contacts List</h1>
<a href="add_contact.html">Add New Contact</a><br/><br/>
 
    <table>
        <tr>
            <th>Name</td>
            <th>Email</td>
            <th>Update</td>
        </tr>
<?php

$result = mysqli_query($connection, "SELECT * FROM Persons"); 
while($query_data = mysqli_fetch_array($result)) {         
            echo "<tr>";
            echo "<td>",$query_data[1], "</td>",
                  "<td>",$query_data[2], "</td>";
            echo "<td><a href=\"edit_contact.php?id=$query_data[0]\">Edit</a> | <a href=\"delete_contact.php?id=$query_data[0]\" onClick=\"return confirm('Are you sure you want to delete?')\">Delete</a></td>";        
        }
        ?>
    </table>
</body>
</html>
