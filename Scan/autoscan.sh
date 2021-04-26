#!/bin/bash

# Network enumeration script written by checkn8
# Just a quick script to help when using Nmap

# Check if valid params were sent 

if [ "$1" == "" ]
then
printf "[-]Syntax: autoscanner <namp ip range> <your IP> " ;

elif [ "$2" == "" ]
then
printf "[-] Invalid Syntax! \n Syntax: autoscanner <namp ip range> <your IP> \n" ;

# Start scanning
else
yellow="\e[93m"

reset="\e[0m"

printf "Your IP is: $2 \n";

# Create a dir to output scans with date and time
currentDate=`date +"%d-%b-%Y_%H:%M"` ;
currentDate=$currentDate | cut -c 1 ;
printf "[+] Saving Scans in /scans_$currentDate \n";
mkdir scans_$currentDate ;

printf "[+] Pinging Network...\n";
nmap -sn -T4 $1 >scans_$currentDate/live_mac_ip.txt;

echo -e "\n[+] Live Targets: ${yellow}\n";
cat scans_$currentDate/live_mac_ip.txt | grep "Nmap scan" | cut -d " " -f 5 | grep -v "$2";
cat scans_$currentDate/live_mac_ip.txt | grep "Nmap scan" | cut -d " " -f 5 | grep -v "$2" > scans_$currentDate/live_ips.txt;
printf "${reset}\n";

printf '[+] Running port and version enumeration: (nmap -T4 -p- -A) \n';

for i in $(<scans_$currentDate/live_ips.txt);do
        #-oA scans_$currentDate/$i for multiple output files. 
	echo -e "${yellow}\n[+] Scanning: $i${reset}";
	printf "\n";
	nmap -T4 -p- -A -vv -oN scans_$currentDate/$i.log $i &
	printf "\n";
wait
done

printf '[+] Saved Scans\n';
fi
