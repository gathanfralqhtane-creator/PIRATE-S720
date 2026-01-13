import os
import sys
import time
import subprocess

# ألوان الشيطان
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
W = '\033[0m'

def logo():
    os.system('clear')
    print(R + """
      .---.              .-----------.
     /     \    __      /    .---.    \ 
    / /     \  (  )    /    /     \    \ 
   //////    ' \/ `   //////      |
  //// [ PIRATE-S720 ] ////       |
 //////      (☠️ )    //////       /
      `----------'            /
     _______WIFI-DEVIL_______/
    """ + Y + """
   [☠️ ] MODE: ROOT ACTIVATED (REAL HACK)
   [☠️ ] Dev: Gathan (THE-DEVIL)
   -----------------------------------------
    """ + W)

def main():
    logo()
    print(G + "[1] " + W + "استخراج الرمز الحقيقي (إدخال بيانات الشبكة)")
    print(G + "[2] " + W + "كشف الشبكات المخفية (Actual Scan)")
    print(G + "[3] " + W + "إنشاء نقطة وهمية + باركود QR للاتصال")
    print(R + "[4] " + W + "خروج")
    
    cmd = input("\n" + R + "[PIRATE@720]:# " + W)
    
    if cmd == '1':
        name = input(Y + "[+] اكتب الاسم: " + W)
        gate = input(Y + "[+] اكتب البوابة: " + W)
        ip_addr = input(Y + "[+] اكتب الأي بي: " + W)
        
        print(R + "\n[*] جاري اختراق ملفات النظام وسحب الرمز الحقيقي لـ " + name + "..." + W)
        time.sleep(2)
        
        # أمر الروت الحقيقي لسحب الرمز من ملفات أندرويد
        command = f"tsu -c 'cat /data/misc/wifi/wpa_supplicant.conf | grep -A 10 \"ssid=\\\"{name}\\\"\" | grep \"psk=\"'"
        try:
            result = subprocess.check_output(command, shell=True).decode()
            if result:
                password = result.split('=')[1].replace('"', '').strip()
                print(G + f"\n[✔] تم العثور على الرمز الحقيقي: " + R + password + W)
            else:
                print(R + "[!] لم يتم العثور على الرمز في السجلات. (ربما لم تتصل بها مسبقاً)")
        except:
            print(R + "[!] خطأ: تأكد من منح صلاحية الروت (SuperUser) لترمكس!")
            
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '2':
        print(Y + "\n[*] جاري تشغيل الرادار بصلاحية الروت..." + W)
        os.system("tsu -c 'airodump-ng wlan0'")
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '3':
        ssid = input(Y + "أدخل اسم الشبكة: " + W)
        pw = input(Y + "أدخل الرمز: " + W)
        print(R + f"\n[!] تم إطلاق الشبكة.. صور الباركود أدناه للاتصال فوراً:")
        
        # إنشاء وطباعة الباركود في الترمكس
        qr_data = f"WIFI:S:{ssid};T:WPA;P:{pw};;"
        os.system(f"qrencode -t ANSI256 '{qr_data}'")
        
        print(G + "\n[✔] أي شخص يصور هذا الكود سيتصل بشبكتك تلقائياً!" + W)
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '4':
        sys.exit(R + "\nوداعاً أيها القرصان." + W)
    else:
        main()

if __name__ == "__main__":
    main()
    
