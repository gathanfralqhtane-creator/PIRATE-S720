#!/bin/bash

# ألوان التميز
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # بدون لون

clear
echo -e "${RED}"
# رسمة بسيطة عند التثبيت
figlet -f small "PIRATE 720"
echo -e "${YELLOW}[*] جارٍ تحضير ترسانة القرصان 720 لهاتفك المروت...${NC}"

# تحديث النظام وحزم ترمكس
pkg update && pkg upgrade -y

# تثبيت الأدوات المطلوبة (tsu للروت، qrencode للباركود، python للأداة)
echo -e "${GREEN}[+] تثبيت الأدوات الأساسية (Python, Tsu, Qrencode, Aircrack-ng)...${NC}"
pkg install python tsu qrencode aircrack-ng figlet ruby curl -y

# تثبيت lolcat لإضافة ألوان احترافية
gem install lolcat

# إعطاء صلاحية التنفيذ للملف الرئيسي
if [ -f "pirate720.py" ]; then
    chmod +x pirate720.py
    echo -e "${GREEN}[✔] تم إعطاء صلاحيات التنفيذ لـ pirate720.py${NC}"
else
    echo -e "${RED}[!] تحذير: ملف pirate720.py غير موجود في المجلد الحالي!${NC}"
fi

echo -e "${GREEN}[✔] اكتمل التثبيت بنجاح!${NC}"
echo -e "${YELLOW}[!] الآن يمكنك إطلاق الأداة بكتابة: python pirate720.py${NC}"
echo -e "${RED}[!] ملاحظة: عند أول تشغيل، وافق على طلب الروت (SuperUser).${NC}"
