<?php

$command = escapeshellcmd('/home/pi/Code/App/strobe.py');
$output = shell_exec($command);
echo $output;

?>