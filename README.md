# 🌙 Dark Mode Proxy (Python)

A Python-based system-wide dark mode engine for browsers like Chrome.
It uses a local proxy to inject dark-mode CSS into all websites in real-time.

## 🚀 Features

* 🌐 Works on all websites
* 🔐 HTTPS support (via mitmproxy)
* 🎛️ GUI control panel
* 🌙 Real-time dark mode injection

## 🛠️ Tech Stack

* Python
* mitmproxy
* PyQt5

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

## 🔧 Manual Steps

* Set proxy to: `127.0.0.1:8080`
* Install certificate via `http://mitm.it`

## ⚠️ Disclaimer

This tool intercepts web traffic locally for modification.
Do not use on sensitive networks.

## 💡 Future Improvements

* Theme system
* Auto proxy setup
* AI brightness control

## 👨‍💻 Author

Mohit Kumar
