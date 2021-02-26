<?php

$command = escapeshellcmd('/home/pi/Code/App/sleep_off.py');
$output = shell_exec($command);
echo $output;

?>

