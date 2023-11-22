<?php

        /**
         * Starts a Minecraft server.
         *
         * Description:
         * This function starts a Minecraft server by executing the necessary commands
         * in the command line. It assumes that the Minecraft server files are already
         * installed and configured on the server machine.
         *
         * Parameters:
         * None
         *
         * Returns:
         * None
         *
         * Examples:
         * startMinecraftServer();
         */

            // Change the directory to the Minecraft server directory
chdir('/home/www-data/lobby');
$fp = fopen("homework.txt", "r+");
$comment = filter_input(INPUT_POST, 'comment', FILTER_SANITIZE_STRING);
//$hw = nl2br($hw);
echo "$comment";
//if(empty($hw)){
//echo "<script>location.reload()</script>";
//} else {

rewind($fp);
fputs($fp, $comment);
//header('Location: h.php');
//echo "<script>location.reload()</script>";
//}         // Start the Minecraft server using the 'java' command

//header('Location: h.php');

?>
<?php
header('Location: h.php');
?>

//<script>location.reload()</script>
