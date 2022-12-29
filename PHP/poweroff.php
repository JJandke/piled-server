<?php

$command = escapeshellcmd('/home/pi/code/python/power_off.py');
$output = shell_exec($command);
echo $output;

?>