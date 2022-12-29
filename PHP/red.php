<?php

$command = escapeshellcmd('/home/pi/code/python/red.py');
$output = shell_exec($command);
echo $output;

?>