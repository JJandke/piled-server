<?php

$command = escapeshellcmd('/home/pi/Code/App/fade.py');
$output = shell_exec($command);
echo $output;

?>