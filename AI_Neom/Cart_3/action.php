<?php
    session_start();
    require '../config.php';
   
    if(isset($_GET['remove'])){
        $id = $_GET['remove'];
        $stmt = $conn->prepare("DELETE FROM InStore_Table WHERE Item=?");
        $stmt->bind_param("s",$id);
        $stmt->execute();
        header('location:/AI_Neom/Cart_3/index.php');

      
   }// This is to delete all items from cart table
   if(isset($_GET['clear'])){
    $stmt = $conn->prepare("DELETE FROM InStore_Table");
    $stmt->execute();
    header('location:/AI_Neom/Cart_3/index.php');


}
?>