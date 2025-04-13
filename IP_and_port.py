import random

def generate_proxy_list(count):
    proxies = []
    for _ in range(count):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        port = random.randint(1024, 65535)
        proxies.append(f"https://{ip}:{port}")
    return proxies

proxy_list = generate_proxy_list(150)
for proxy in proxy_list:
    print(proxy)
