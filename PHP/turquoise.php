<?php

$command = escapeshellcmd('/home/pi/Code/App/turquoise.py');
$output = shell_exec($command);
echo $output;

?>