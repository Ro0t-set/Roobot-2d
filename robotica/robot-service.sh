#!/bin/sh
### BEGIN INIT INFO
# Provides: robot
# Required-Start:
# Required-Stop:
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Avvio automatico del sito
# Description: Servizio per ovviare il precedente malfuzionante
### END INIT INFO

DESC="robot"
NAME=tobot-service
alias proj="cd /home/django/django_project"

do_start()
{
   echo "starting!";

   #sudo apt-get install dnsmasq hostapd
   #ip :    sudo nano /etc/dhcpcd.conf
   #interface wlan0
   # static ip_address=192.168.4.1
   #sudo service dhcpcd restart 


   cd /home/Dersktop/Roobot-2d/robotica;
   echo "Trovata Cartella!!";
   sudo ifdown wlan0
   sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf
   exec python3 manage.py runserver 192.168.4.1:8000 &;
   echo "Avvio eseguito con successo!";
}


do_stop()
{
   echo "stopping!"
}


case "$1" in
   start)
     do_start
     ;;
   stop)
     do_stop
     ;;
esac