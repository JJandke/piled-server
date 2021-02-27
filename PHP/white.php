<?php

$command = escapeshellcmd('/home/pi/Code/App/white.py');
$output = shell_exec($command);
echo $output;

?>