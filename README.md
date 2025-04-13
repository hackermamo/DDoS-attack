# 🔥 Multi-threaded HTTP Load Tester (with Optional Proxy Support)

This is a Python-based multi-threaded HTTP load tester designed to stress test a web server by sending repeated HTTP requests using customizable headers, threading, and optional proxy support.

> ⚠️ **Disclaimer:** This tool is for educational and authorized testing purposes **only**. Do not use it on servers you do not own or do not have permission to test.

---

## 🚀 Features

- Multi-threaded request spamming.
- Optional proxy list support.
- Randomized realistic HTTP headers (User-Agent, Referer).
- Timeout customization.
- Lightweight and easy to run.

---

## 📦 Requirements

- Python 3.x
- `requests` library

To install the `requests` library:

```bash
pip install requests
```

🧑‍💻How To use 

> Clone or copy this script into a file, e.g., load_tester.py.

> Prepare a file containing HTTP/S proxy addresses (optional).

> Run the script:

>bash
```
python DDoS.py
```
> Enter the prompted input:

> Target URL – the website or server to test (e.g., http://example.com or http://localhost)

>Proxy file path – optional path to a .txt file with proxies (IP:PORT or http://IP:PORT). Leave blank if not using proxies.

> Number of threads – number of concurrent threads (e.g., 100).

> Request timeout – timeout per request in seconds.
