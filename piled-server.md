# piled-server
Server side code for the Piled project. (Controlling an RGB strip using an Android app and Raspberry Pi.)

------

To be able to use the Raspberry Pi as a server, it still needs to be configured a bit. 

1. **Create a directory for the log files and a log file for cronjobs.**

   ```shell
   mkdir log
   cd /log
   touch cron.log
   cd
   ```

   

2. **Create a directory for the Python scripts.**

   ```shell
   mkdir /Code/App
   cd /Code/App
   ```

   now, paste the Python Files in here.

   

3. **Change the read and write permissions of the Python scripts** so that they can be executed by others.

   ```shell
   sudo chmod 755 /home/pi/Code/App/*
   ```

   

4. **Launch the "pigpiod" service**

   ```sh
   sudo pigpiod
   ```

   

5. **In order for "pigpiod" to be executed at every boot, the following line must be added to the root crontab.**

   ```shell
   sudo crontab -e
   @reboot pigpiod > /home/pi/log/cron.log 2>&1
   ```

   

6. **Install the Apache2 server**

   ```shell
   sudo apt-get install apache2
   sudo chown -R pi /var/www/
   ```

   Now the Raspberry Pi should be accessible in the home network at http://raspberrypi.
   A welcome page will be displayed at this URL.

   

7. **Install PHP and related packages**

   ```shell
   sudo apt-get install php libapache2-mod-php
   ```

   

8. **Now add the PHP files under /var/www/html**

   

9. **And give the logfile for the piled project the rights so that others than the Pi user can write.**

   ```sh
   sudo chmod 666 /home/pi/log/piled.log
   ```

   If no Python script has been executed yet, no logfile exists. Alternatively, it can of course also be created with this:

   ```shell
   touch /home/pi/log/piled.log
   ```

   

10. **For the Python scripts executed by *www-data* to work correctly, read and write permissions for */dev/mem* must be assigned** 

    ```shell
    sudo chmod g+rw /dev/mem
    ```

    At this point, [this page in particular](https://raspberrypi.stackexchange.com/questions/40105/access-gpio-pins-without-root-no-access-to-dev-mem-try-running-as-root) has helped me.

