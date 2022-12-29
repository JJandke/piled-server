<?php

$command = escapeshellcmd('/home/pi/code/python/white.py');
$output = shell_exec($command);
echo $output;

?>