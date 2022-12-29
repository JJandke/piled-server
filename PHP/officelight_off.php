<?php

$command = escapeshellcmd('/home/pi/code/python/officelight_off.py');
$output = shell_exec($command);
echo $output;

?>

