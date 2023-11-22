<!DOCTYPE html>
<html>
<head>
<title>Hausaufgaben eintragen</title>
<meta charset="utf-8">
<link rel="stylesheet" href="edit/phpkid.css">
</head>
<body>
</body>
</html>

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
$fp = fopen("homework.txt", "r");
$hw = file_get_contents('homework.txt');
echo <<<FORM
<form action="hw.php" method="post">
<textarea cols="110" rows="8" name="comment">$hw</textarea>
<input type="submit" value="Eintragen">
</form>
FORM;
            // Start the Minecraft server using the 'java' command
        ?>
