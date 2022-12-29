<?php

$command = escapeshellcmd('/home/pi/code/python/officelight_on.py');
$output = shell_exec($command);
echo $output;

?>

