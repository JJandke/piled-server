<?php

$command = escapeshellcmd('/home/pi/Python/App/orange.py');
$output = shell_exec($command);
echo $output;

?>