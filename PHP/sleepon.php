<?php

$command = escapeshellcmd('/home/pi/Code/App/sleep_on.py');
$output = shell_exec($command);
echo $output;

?>

