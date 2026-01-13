import os
import sys
import time

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
   [☠️ ] MODE: NORMAL (NO-ROOT SAFE)
   [☠️ ] Dev: Gathan (THE-DEVIL)
   -----------------------------------------
    """ + W)

def main():
    logo()
    print(G + "[1] " + W + "استخراج الرمز (تحليل البيانات الذكي)")
    print(G + "[2] " + W + "كشف الشبكات المحيطة")
    print(G + "[3] " + W + "إنشاء نقطة وهمية + باركود QR")
    print(R + "[4] " + W + "خروج")
    
    cmd = input("\n" + R + "[PIRATE@720]:# " + W)
    
    if cmd == '1':
        name = input(Y + "[+] اكتب اسم الشبكة: " + W)
        gate = input(Y + "[+] اكتب البوابة: " + W)
        ip = input(Y + "[+] اكتب الأي بي: " + W)
        
        print(R + "\n[*] جاري الاتصال بالبوابة " + gate + " واختراق الحماية...")
        time.sleep(3)
        print(G + "[+] تم كسر تشفير الحزمة المستلمة من " + ip)
        time.sleep(1)
        
        # كود يقوم بتوليد رمز بناءً على اسم الشبكة (للمحاكاة الاحترافية)
        simulated_pass = name + "@2026"
        print(G + f"\n[✔] الرمز المستخرج لـ {name} هو: " + R + simulated_pass + W)
        print(Y + "[!] ملاحظة: بدون روت، هذا هو الرمز الأقرب للاختراق." + W)
            
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '2':
        print(Y + "\n[*] جاري فحص الشبكات المتاحة..." + W)
        os.system("nmcli dev wifi list || termux-wifi-scanlist")
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '3':
        ssid = input(Y + "اسم الشبكة الوهمية: " + W)
        pw = input(Y + "الرمز: " + W)
        print(R + f"\n[!] الفخ جاهز.. صور الباركود للاتصال:")
        qr_data = f"WIFI:S:{ssid};T:WPA;P:{pw};;"
        os.system(f"qrencode -t ANSI256 '{qr_data}'")
        input("\nاضغط Enter للعودة..."); main()
        
    elif cmd == '4':
        sys.exit(R + "\nوداعاً." + W)
    else:
        main()

if __name__ == "__main__":
    main()
    
