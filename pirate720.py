import os
import sys
import time
import itertools
import string

# ألوان التنسيق
R = '\033[1;31m' # أحمر
G = '\033[1;32m' # أخضر
Y = '\033[1;33m' # أصفر
C = '\033[1;36m' # سماوي
W = '\033[1;37m' # أبيض
RESET = '\033[0m'

def logo():
    os.system('clear')
    # رسمة الجمجمة الجديدة (القرصان)
    print(R + """
                          ______
                       .-"      "-.
                      /            \\
                     |              |
                     |,  .-.  .-.  ,|
                     | )(__/  \__)( |
                     |/     /\     \|
           _         (_     ^^     _)        _
          / \         \__|IIIIII|__/        / \\
         |   |         | \IIIIII/ |        |   |
         \    \_       \          /      _/    /
          \     "---____"----------"____---"     /
           \                                   /
            "---____Pirate-S720_v2.0____---"
    """ + Y + """
     [☠️ ] Dev: Gathan | [☠️ ] Type: Ultra Brute Force
    -----------------------------------------------
    """ + RESET)

def brute_force():
    ssid = input(C + "[+] اسم الشبكة المستهدفة: " + RESET)
    print(R + "[*] بدء محرك التخمين الشامل (0-9 / A-Z / a-z)..." + RESET)
    
    # قائمة الرموز الشاملة: أرقام + حروف كبيرة + حروف صغيرة
    chars = string.digits + string.ascii_letters
    
    count = 0
    start_time = time.time()
    
    try:
        # التخمين يبدأ من طول 8 رموز (الحد الأدنى للواي فاي)
        for length in range(8, 13):
            for attempt in itertools.product(chars, repeat=length):
                password = "".join(attempt)
                
                # طباعة التخمين الحالي بسرعة فائقة في نفس السطر
                sys.stdout.write(f"\r{W}[-] فحص الرمز: {G}{password}{RESET} | محاولات: {Y}{count}{RESET}")
                sys.stdout.flush()
                
                count += 1
                
                # شرط توقف افتراضي للتجربة (يمكنك تغييره)
                if password == "ali12345":
                    end_time = time.time()
                    print(f"\n\n{G}[✔] تم كسر التشفير! الرمز هو: {R}{password}{RESET}")
                    print(f"{Y}[*] الوقت المستغرق: {round(end_time - start_time, 2)} ثانية.")
                    return
    except KeyboardInterrupt:
        print(R + "\n\n[!] تم إيقاف الهجوم يدوياً." + RESET)

def main():
    logo()
    print(G + "[1] " + W + "التخمين الخارق (أرقام + حروف)")
    print(G + "[2] " + W + "فتح بوابة الراوتر (IP Gateway)")
    print(G + "[3] " + W + "إنشاء فخ باركود QR")
    print(R + "[4] " + W + "خروج")
    
    choice = input("\n" + R + "[PIRATE@720]:# " + RESET)
    
    if choice == '1':
        brute_force()
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '2':
        gate = input(C + "[+] أدخل البوابة (مثلاً 192.168.1.1): " + RESET)
        os.system(f"termux-open-url http://{gate}")
        main()
    elif choice == '3':
        name = input(C + "[+] اسم شبكة الفخ: " + RESET)
        pw = input(C + "[+] رمز الفخ: " + RESET)
        os.system(f"qrencode -t ANSI256 'WIFI:S:{name};T:WPA;P:{pw};;'")
        input("\nاضغط Enter للعودة..."); main()
    elif choice == '4':
        sys.exit(R + "وداعاً أيها القرصان." + RESET)
    else:
        main()

if __name__ == "__main__":
    main()
    
