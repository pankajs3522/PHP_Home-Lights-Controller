<?php 
$myfile = fopen("status.txt","r+");
$txt = $_GET['v'];
fwrite($myfile, $txt);
fclose($myfile);
?>