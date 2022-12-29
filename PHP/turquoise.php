<?php

$command = escapeshellcmd('/home/pi/code/python/turquoise.py');
$output = shell_exec($command);
echo $output;

?>