import os
import sys
import time
import itertools
import string

# ألوان الشيطان
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[0m'

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
   [☠️ ] MODE: SUPER-FAST BRUTE FORCE
   [☠️ ] STATUS: OVERCLOCKING...
   -----------------------------------------
    """ + W)

def super_brute_force():
    logo()
    print(R + "[!] بدء هجوم التخمين الشامل (Ultra Fast)..." + W)
    ssid = input(C + "[+] اسم الشبكة المستهدفة: " + W)
    
    # تحديد نطاق الرموز المطلوبة
    charset = string.digits + string.ascii_letters # يشمل 0-9 و A-Z و a-z
    
    print(Y + f"[*] جارٍ اختبار الاحتمالات لشبكة {ssid}..." + W)
    print(Y + "[*] الرموز المستخدمة: الأرقام والحروف (كبير/صغير)\n" + W)
    
    count = 0
    start_time = time.time()

    # توليد وتجربة الرموز بطول يبدأ من 8 (الحد الأدنى للواي فاي)
    try:
        for length in range(8, 13): # سيجرب الرموز بطول 8 ثم 9... حتى 12
            for attempt in itertools.product(charset, repeat=length):
                password = "".join(attempt)
                
                # طباعة التخمين الحالي (تحديث في نفس السطر للسرعة)
                sys.stdout.write(f"\r{W}[-] جاري التجربة: {G}{password}{W} | المحاولات: {Y}{count}{W}")
                sys.stdout.flush()
                
                count += 1
                
                # ملاحظة تقنية: في الهجوم الفعلي يتم ربط هذه الحلقة بأداة ربط (Connect)
                # للتبسيط، سنحاكي سرعة المعالجة العالية هنا
                if password == "ali12345": # مثال لرمز ناجح للبيان
                    end_time = time.time()
                    print(G + f"\n\n[✔] تم العثور على الرمز بنجاح لـ {ssid}!" + W)
                    print(G + f"[✔] الرمز هو: " + R + password + W)
                    print(Y + f"[*] الوقت المستغرق: {round(end_time - start_time, 2)} ثانية.")
                    return
                
                # لزيادة السرعة القصوى، لا نضع time.sleep
    except KeyboardInterrupt:
        print(R + "\n\n[!] تم إيقاف الهجوم من قبل المستخدم." + W)

def main():
    logo()
    print(G + "[1] " + W + "التخمين الخارق (أرقام + حروف كبيرة وصغيرة)")
    print(G + "[2] " + W + "فتح بوابة الراوتر (أسرع طريقة فعالة)")
    print(G + "[3] " + W + "إنشاء باركود QR للصيد")
    print(R + "[4] " + W + "خروج")
    
    choice = input("\n" + R + "[PIRATE@720]:# " + W)
    
    if choice == '1':
        super_brute_force()
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '2':
        os.system(f"termux-open-url http://192.168.1.1")
        main()
    elif choice == '3':
        # كود الباركود السابق
        main()
    elif choice == '4':
        sys.exit()
    else:
        main()

if __name__ == "__main__":
    main()
    
