<?php

$command = escapeshellcmd('/home/pi/code/python/yellow.py');
$output = shell_exec($command);
echo $output;

?>