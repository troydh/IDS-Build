import re
import argparse
from collections import defaultdict

# Settings
THRESHOLD = 5
ALERT_LOG = "logs/detected_intrusions.log"

def detect_brute_force(log_file):
    failed_attempts = defaultdict(int)

    with open(log_file, 'r') as file:
        for line in file:
            if "Failed password" in line:
                match = re.search(r'from\s+(\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1

    with open(ALERT_LOG, 'w') as alert_file:
        for ip, count in failed_attempts.items():
            if count >= THRESHOLD:
                alert = f"[ALERT] Potential SSH brute force attack detected from IP: {ip} ({count} failed attempts)\n"
                print(alert.strip())
                alert_file.write(alert)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Brute Force IDS")
    parser.add_argument("--log", required=True, help="Path to system auth log or test log")
    args = parser.parse_args()

    detect_brute_force(args.log)
