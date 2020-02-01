<?php include_once("../inc/dbinfo.inc");
include_once("header.php"); ?>
<html>
<body>
<h1>Update Contact</h1>
<?php
if(isset($_POST['update']))
{    
    $id = $_POST['id'];
    
    $name=$_POST['name'];
    $email=$_POST['email'];    
    
    // Checke the fields
    if(empty($name) || empty($email)) {            
        if(empty($name)) {
            echo "<p class='fail'>Please enter the name!</p><br/>";
        }
        
        if(empty($email)) {
            echo "<p class='fail'>Please enter the email!</p><br/>";
        }        
    } else {    
        //updating the table
        $result = mysqli_query($connection, "UPDATE Persons SET name='$name',email='$email' WHERE id=$id");

        //return to home page index.php
        header("Location: index.php");
    }
}
?>
<?php
//getting id from url
$id = $_GET['id'];
 
//retrieve contact by id
$result = mysqli_query($connection, "SELECT * FROM Persons WHERE id=$id");
 
while($query_data = mysqli_fetch_array($result))
{
    $name = $query_data[1];
    $email = $query_data[2];
}
?>
<a href="index.php">Home</a>
    <br/><br/>
    
    <form name="form1" method="post" action="edit_contact.php">
        <table border="0">
            <tr> 
                <td>Name</td>
                <td><input type="text" name="name" value="<?php echo $name;?>"></td>
            </tr>
            <tr> 
                <td>Email</td>
                <td><input type="text" name="email" value="<?php echo $email;?>"></td>
            </tr>
            <tr>
                <td><input type="hidden" name="id" value=<?php echo $_GET['id'];?>></td>
                <td><input type="submit" name="update" value="Update"></td>
            </tr>
        </table>
    </form>
</body>
</html>
