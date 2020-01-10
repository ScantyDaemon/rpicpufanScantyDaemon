# Raspberry Pi cpu Fan + shutdown button
rip cpu fan + shutdown button

1.Use chip transistor like bc547.

2.Control transistor pin connected to pin 2 gpio.

3.cpu fan "+" pin connect to transistor, "-" pin connect to any GND.

4.For shutdown button use resistor 1kom-3kom and connect to pin 18 gpio and any and pin.

5. download python 3 and all dependencies.

6. make new systemcl daemon with following code and change "NAMEOFYOURSERVICE" on your name: nano /lib/systemd/system/NAMEOFYOURSERVICE.service
  
Then paste this code:

[Unit]
Description=NAMEOFYOURSERVICE Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/temp.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target


7. copy file temp.py into /home/pi/temp.py

8. Load Ned deamon with command: systemctl daemon-reload

9. systemctl start NAMEOFYOURSERVICE

10. systemctl status NAMEOFYOURSERVICE

