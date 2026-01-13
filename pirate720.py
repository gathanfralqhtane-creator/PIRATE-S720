import os
import sys
import time

# ألوان الهكر (أحمر، أخضر، أصفر)
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
W = '\033[0m'

def clear():
    os.system('clear')

def logo():
    print(R + """
      .---.              .-----------.
     /     \    __      /    .---.    \ 
    / /     \  (  )    /    /     \    \ 
   //////    ' \/ `   //////      |
  //// [  PIRATE-S720 ] ////      |
 //////      (☠️ )    //////       /
      `----------'            /
     _______WIFI-DEVIL_______/
    """ + Y + """
   [☠️ ] Developer: Gathan (THE-DEVIL)
   [☠️ ] Status: Pirate Mode Activated
   -----------------------------------------
    """ + W)

def main():
    clear()
    logo()
    print(G + "[1] " + W + "استخراج رمز الشبكة (يدوي عبر IP والـ Gateway)")
    print(G + "[2] " + W + "كشف الشبكات المخفية المحيطة")
    print(G + "[3] " + W + "إنشاء نقطة وهمية (Evil Twin) لاصطياد الضحايا")
    print(R + "[4] " + W + "خروج")
    
    cmd = input("\n" + R + "[PIRATE@720]:# " + W)
    
    if cmd == '1':
        name = input(Y + "[+] اسم الشبكة المستهدفة: " + W)
        gate = input(Y + "[+] عنوان البوابة (Gateway): " + W)
        ip = input(Y + "[+] عنوان الأي بي (IP): " + W)
        print(R + "\n[*] جارٍ تحليل البيانات واختراق التشفير..." + W)
        time.sleep(3)
        # محاكاة استخراج الرمز
        print(G + f"[✔] تم فك التشفير! الرمز هو: " + R + "P@ss_Gathan720" + W)
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '2':
        print(Y + "\n[*] جارٍ تشغيل الرادار لكشف الإشارات المخفية..." + W)
        os.system("airodump-ng wlan0")
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '3':
        ssid = input(Y + "اسم الشبكة الوهمية: " + W)
        pw = input(Y + "رمز الشبكة للصيد: " + W)
        print(R + f"\n[!] تم إطلاق {ssid}.. الشيطان ينتظر الضحايا..." + W)
        # إنشاء باركود للاتصال السريع
        os.system(f"qrencode -t ANSI256 'WIFI:S:{ssid};T:WPA;P:{pw};;'")
        print(G + "[✔] اجعل الضحية يصور الباركود للاتصال فوراً!" + W)
        input("\nاضغط Enter للإغلاق..."); main()
        
    elif cmd == '4':
        sys.exit(R + "\nوداعاً أيها القرصان." + W)
    else:
        main()

if __name__ == "__main__":
    main()
  
