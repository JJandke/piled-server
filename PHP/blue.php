<?php

$command = escapeshellcmd('/home/pi/Code/App/blue.py');
$output = shell_exec($command);
echo $output;

?>