# Lightweight IDS - Brute Force SSH Detector 🚨

A simple Python-based Intrusion Detection System (IDS) that monitors system authentication logs for brute-force SSH login attempts and generates alerts.

## 🔍 Features
- Detects multiple failed login attempts from the same IP
- Alerts when a threshold is exceeded
- Lightweight and customizable
- Log parsing from `/var/log/auth.log` or test logs
- Easy to extend with additional rules

## 🧰 Requirements

Install dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🚀 How to Use

```bash
python ids.py --log test/sample_auth_log.txt
```

## ⚙️ Configuration

You can modify the detection threshold and log path at the top of `ids.py`.

## 📁 Project Structure

```
lightweight-ids/
├── ids.py                   # Main IDS script
├── requirements.txt         # Required Python libraries
├── README.md                # Project documentation
├── logs/                    # Output logs
│   └── detected_intrusions.log
├── test/
│   └── sample_auth_log.txt  # Sample log file for testing
```

## 📸 Example Alert

```
[ALERT] Potential SSH brute force attack detected from IP: 192.168.1.100 (15 failed attempts)
```

## 🪪 License

MIT License

---

> Created for cybersecurity learning and portfolio demonstration.
