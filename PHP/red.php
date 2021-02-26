<?php

$command = escapeshellcmd('/home/pi/Code/App/red.py');
$output = shell_exec($command);
echo $output;

?>