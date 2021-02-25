<?php 

$command = escapeshellcmd('/home/pi/Code/App/multistrobe.py');
$output = shell_exec($command);
echo $output;

?>