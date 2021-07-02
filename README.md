# piled-server
Server side code for the Piled project. (Controlling an RGB strip using an Android app and Raspberry Pi.)

------
# piled-server

Server side code for the Piled project. (Controlling an RGB strip using an Android app and Raspberry Pi.)

------

## Hardware

**To connect the LED strip to the Raspberry Pi, you still need the following components:**

- [The 12V LED strip](https://www.amazon.de/dp/B087B49JD7/) 

- [Circuit board](https://www.amazon.de/dp/B0734XYJPM/) or [breadboard](https://www.amazon.de/dp/B07VFK5CRP/)

- [Jumper cables](https://www.amazon.de/dp/B01EV70C78/)

- [3x N-channel MosFets](https://www.amazon.de/dp/B01FUSRARW/)



**I have now connected the LED strip as following:**

- First we have to solder three **MosFets** to the board or plug them to the breadboard. When soldering you should be careful not to solder too hot, otherwise the MosFets will break quickly.
- Then we have to connect three **GPIO** pins `(e.g. GPIO16, GPIO20, GPIO21)` with jumper cables to the **Gate** of the MosFet. Further we connect the **GND** of the Pi to the blue **GND** **rail** on the breadboard.
- As a 3rd step we connect the **Source** pins of the MosFets to the same **GND** rail where we connected the GND of the Raspberry Pi.
- Now we only have to connect the LED strip. For this we connect the **+12V** of the LED band to the positive red **rail** of the breadboard.
  The three **colors** are connected to the **Drain** pin of the MosFet.
- If we now connect the **+12V** and **GND** of the power supply to the **respective** **rails** of the breadboard, the LED band could already be controlled.


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

