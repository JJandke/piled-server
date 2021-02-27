<?php

$command = escapeshellcmd('/home/pi/Code/App/yellow.py');
$output = shell_exec($command);
echo $output;

?>