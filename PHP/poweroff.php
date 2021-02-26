<?php

$command = escapeshellcmd('/home/pi/Code/App/power_off.py');
$output = shell_exec($command);
echo $output;

?>