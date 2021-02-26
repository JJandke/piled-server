<?php

$command = escapeshellcmd('/home/pi/Code/App/orange.py');
$output = shell_exec($command);
echo $output;

?>