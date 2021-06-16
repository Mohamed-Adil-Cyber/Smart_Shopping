<?php
$host = "remotemysql.com";
$user = "VLwIyxlKeg";
$passwd = "RPAo4fNBiy";
$database = "VLwIyxlKeg";
$conn = new mysqli($host, $user, $passwd, $database);
if ($conn->connect_error) {
    die("Connection error: " . $conn->connect_error);
}
?>
