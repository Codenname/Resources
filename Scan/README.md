# Tools
Small collection of little scripts for pentesting

(Nothing here is earth shattering, it's just small collection of scripts that I find to save a little bit of time)

### Autoscan:
-------------------------------------------
Autoscan runs a nmap ping scan and ouputs the live hosts to a file and excludes your ip from the list. It then runs individual scans on each ip and ouputs them into a date/time labeled folder and individually named .log file. For example a machine at 10.0.2.110 will be 10.0.2.110.log
Just a nice little tool to keep your scans organized and documented for further examination.

#### Syntax: 
> ./autoscan.sh (nmap ip range) (your current ip on the network you are testing)
##### Example:
> ./autoscan.sh 10.2.0.0/24 10.2.0.100

---------------------------------------------------

### Penstart:

Penstart is a simple script that sets up a dir with named whatever you want. The dir includes a exploits, gobuster_scans, and nikto scans dir. It also sets up a readme file with the target name you inputted as the header.

I will be updating this to include more folders and more advanced documentation set up as I progress in my pentest learning.

My philosophy is to stay as organized as you can during a pentest for easy report writing. 

> Syntax: penstart.sh (root folder name)

-----------------------------------

### Pyscrapper:

Simple Python webscrapper that grabs the text from a url and converts it into a txt file readyfor brute force attacks. 

#### Syntax:
> ./pyscrapper -u https://google.com
------------------------------------------
