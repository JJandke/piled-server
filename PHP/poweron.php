<?php

$command = escapeshellcmd('/home/pi/Code/App/power_on.py');
$output = shell_exec($command);
echo $output;

?>