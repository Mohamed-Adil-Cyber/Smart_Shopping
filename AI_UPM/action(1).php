<?php
    session_start();
    require 'config.php';
   
    if(isset($_GET['remove'])){
        $id = $_GET['remove'];
        $stmt = $conn->prepare("DELETE FROM Products_Table WHERE Product_ID=?");
        $stmt->bind_param("i",$id);
        $stmt->execute();

      
   }// This is to delete all items from cart table
?>