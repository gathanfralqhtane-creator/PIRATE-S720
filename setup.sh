#!/bin/bash
clear
echo -e "\e[1;31m"
figlet "PIRATE 720"
echo -e "\e[1;33m[*] جارٍ تجهيز ترسانة القرصان 720...\e[0m"
pkg update && pkg upgrade -y
pkg install python qrencode aircrack-ng figlet ruby curl -y
gem install lolcat
chmod +x pirate720.py
echo -e "\e[1;32m[+] اكتمل التثبيت! الشيطان جاهز للعمل.\e[0m"
