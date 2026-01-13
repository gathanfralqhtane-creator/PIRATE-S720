import os
import sys
import time

# تعريف الألوان للهوية البصرية (رعب)
R = '\033[1;31m' # أحمر
G = '\033[1;32m' # أخضر
Y = '\033[1;33m' # أصفر
C = '\033[1;36m' # سماوي
W = '\033[0m'    # أبيض

def logo():
    os.system('clear')
    print(R + """
      .---.              .-----------.
     /     \\    __      /    .---.    \\
    / /     \\  (  )    /    /     \\    \\
   //////    ' \\/ `   //////      |
  //// [  PIRATE-S720 ] ////      |
 //////      (☠️ )    //////       /
      `----------'            /
     _______WIFI-DEVIL_______/
    """ + Y + """
   [☠️ ] Developer: Gathan (THE-DEVIL)
   [☠️ ] System: Advanced Network Auditor
   -----------------------------------------
    """ + W)

def brute_force_simulation():
    print(R + "\n[*] بدء هجوم القوة الغاشمة (Brute Force)..." + W)
    ssid = input(C + "[+] أدخل اسم الشبكة المستهدفة: " + W)
    print(Y + "[!] جاري تحميل قائمة كلمات المرور (wordlist.txt)..." + W)
    time.sleep(2)
    
    # محاكاة تجربة كلمات المرور
    passwords = ["12345678", "password", "admin123", "00000000", "p@ssword"]
    for password in passwords:
        print(W + f"[-] تجربة الرمز: {password} " + R + "-> فشل" + W)
        time.sleep(0.5)
    
    print(G + "\n[!] تحذير: الهجوم يتطلب وقتاً طويلاً وقائمة كلمات ضخمة." + W)
    print(Y + "[*] نصيحة: استخدم أداة Aircrack-ng للهجمات الفعلية على الـ Handshake." + W)

def open_router_gateway():
    gate = input(C + "[+] أدخل عنوان البوابة (مثال: 192.168.1.1): " + W)
    print(R + "[*] محاولة الاتصال بلوحة تحكم الراوتر..." + W)
    time.sleep(1)
    print(G + "[+] تم العثور على البوابة. يتم الفتح في المتصفح الآن..." + W)
    # فتح الرابط في متصفح الهاتف
    os.system(f"termux-open-url http://{gate}")
    print(Y + "\n[!] جرب الدخول بـ (admin / admin) لسحب الرمز الحقيقي." + W)

def generate_qr():
    ssid = input(C + "[+] اسم الشبكة للفخ: " + W)
    pw = input(C + "[+] الرمز السري للفخ: " + W)
    print(R + "\n[!] توليد باركود QR للاتصال التلقائي..." + W)
    qr_data = f"WIFI:S:{ssid};T:WPA;P:{pw};;"
    os.system(f"qrencode -t ANSI256 '{qr_data}'")
    print(G + "[✔] الباركود جاهز. أي ضحية تصوره ستتصل فوراً!" + W)

def main():
    logo()
    print(G + "[1] " + W + "هجوم القوة الغاشمة (Brute Force)")
    print(G + "[2] " + W + "اختراق البوابة (Router Login)")
    print(G + "[3] " + W + "إنشاء باركود QR للصيد")
    print(R + "[4] " + W + "خروج")
    
    choice = input("\n" + R + "[PIRATE@720]:# " + W)
    
    if choice == '1':
        brute_force_simulation()
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '2':
        open_router_gateway()
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '3':
        generate_qr()
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '4':
        print(R + "إغلاق النظام.. الشيطان يودعك." + W)
        sys.exit()
    else:
        main()

if __name__ == "__main__":
    main()
    
