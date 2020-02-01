<?php
define('DB_SERVER', '<dbinstance-endpoint>');
define('DB_USERNAME', '<master-username>');
define('DB_PASSWORD', '<master-username-password>');
define('DB_DATABASE', 'test');

$connection = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);

if (mysqli_connect_errno()) echo "Failed to connect to MySQL: " . mysqli_connect_error();
?>

