<?php

$command = escapeshellcmd('/home/pi/code/python/orange.py');
$output = shell_exec($command);
echo $output;

?>