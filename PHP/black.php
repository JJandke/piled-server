<?php

$command = escapeshellcmd('/home/pi/Code/App/black.py');
$output = shell_exec($command);
echo $output;

?>