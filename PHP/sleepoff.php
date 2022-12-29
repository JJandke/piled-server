<?php

$command = escapeshellcmd('/home/pi/code/python/sleep_off.py');
$output = shell_exec($command);
echo $output;

?>

