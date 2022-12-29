<?php

$command = escapeshellcmd('/home/pi/code/python/sleep_on.py');
$output = shell_exec($command);
echo $output;

?>

