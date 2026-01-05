import subprocess
import time

UBUNTU_IP = "192.168.1.106"
USER = "fakeuser"
WRONG_PASSWORD = "321"
ATTEMPTS = 8

print(f"[+] Simulating {ATTEMPTS} failed SSH logins to {USER}@{UBUNTU_IP}")

for i in range(1, ATTEMPTS + 1):
    print(f"    Attempt {i}/{ATTEMPTS}")
    subprocess.run(
        [
            "sshpass", "-p", WRONG_PASSWORD,
            "ssh",
            "-o", "PreferredAuthentications=password",
            "-o", "PubkeyAuthentication=no",
            "-o", "StrictHostKeyChecking=no",
            "-o", "UserKnownHostsFile=/dev/null",
            "-o", "ConnectTimeout=5",
            f"{USER}@{UBUNTU_IP}",
            "exit"
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(1)

print("[+] Done. Check /var/log/auth.log and Splunk for 'Failed password' events.")
