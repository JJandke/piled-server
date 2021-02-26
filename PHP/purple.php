<?php

$command = escapeshellcmd('/home/pi/Code/App/purple.py');
$output = shell_exec($command);
echo $output;

?>