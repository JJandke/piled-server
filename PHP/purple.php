<?php

$command = escapeshellcmd('/home/pi/code/python/purple.py');
$output = shell_exec($command);
echo $output;

?>