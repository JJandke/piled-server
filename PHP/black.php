<?php

$command = escapeshellcmd('/home/pi/Python/App/black.py');
$output = shell_exec($command);
echo $output;

?>