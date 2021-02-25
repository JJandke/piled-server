<?php

$command = escapeshellcmd('/home/pi/Code/App/green.py');
$output = shell_exec($command);
echo $output;

?>