<?php

$command = escapeshellcmd('/home/pi/code/python/power_on.py');
$output = shell_exec($command);
echo $output;

?>