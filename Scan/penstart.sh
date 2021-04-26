#!/bin/bash
if [ "$1" == "" ]
then
    echo "Syntax: penstart <root folder name>";
else
    mkdir $1;
    cd $1;
    mkdir "exploits"
    mkdir "gobuster_scans" ;
    mkdir "nikto_scan"
    echo "# $1" > README.md;
    gedit README.md & # Or insert your favorite text editor 
    fi
