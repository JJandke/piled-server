<?php

/* The script is called strobe.php although it does not call strobe.py but multistrobe.py.
But since strobe.py is not used, I have the name available and can use it in the URL, so the URL won't be so long. */

$command = escapeshellcmd('/home/pi/Code/App/strobe.py');
$output = shell_exec($command);
echo $output;

?>