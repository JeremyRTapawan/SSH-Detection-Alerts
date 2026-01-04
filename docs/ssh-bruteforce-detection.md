## Screenshots & Evidence

### 01 — Network Configuration Verification
![ipkali](https://github.com/user-attachments/assets/5038dc65-789c-48d8-ac35-4e7ee3e38420)
![ipubuntu](https://github.com/user-attachments/assets/5a56987c-b7b9-4fb4-b6b4-8c66c67b56e5)

This screenshot verifies that the Kali and Ubuntu virtual machines are on the same internal network and reachable within the same subnet, ensuring proper connectivity for SSH traffic and log generation.

---

### 02 — SSH Service Running on Ubuntu
![sshrunning](https://github.com/user-attachments/assets/dfcf769b-697b-41c9-a785-14dc00d57f9d)

This screenshot confirms that the OpenSSH service is active and listening on port 22 on the Ubuntu system, allowing SSH authentication attempts to be logged and monitored.

---

### 03 — SSH Failed Authentication Logs
![authlogs](https://github.com/user-attachments/assets/435a0c67-e020-4980-92be-54209de82e90)
Linux authentication logs showing multiple failed SSH login attempts generated during attack simulation, serving as the primary data source for brute-force detection.

---

### 04 — Log Ingestion into Splunk
![Splunklogs](https://github.com/user-attachments/assets/541e56d9-1fe1-4604-9690-c18ecb18caa6)

Splunk search results confirming successful ingestion of Linux authentication logs, validating end-to-end log forwarding from the Ubuntu host to the SIEM.

---

### 05 — SSH Brute Force Detection Query

![query](https://github.com/user-attachments/assets/6bcec3a9-39af-44db-acd4-f5c9e4b220dc)

Detection logic correlating multiple failed SSH login attempts from the same source within a short time window to identify potential brute-force activity.

---

### 06 — Alert Configuration
![rules](https://github.com/user-attachments/assets/d36eb0d7-c221-4dda-bc18-d3bc2cb2afec)

Alert configuration showing scheduled execution, time window selection, and threshold-based triggering used to generate alerts when brute-force behavior is detected.

---

### 07 — Triggered SSH Brute Force Alert
![sshtrigger](https://github.com/user-attachments/assets/e6168705-3fa9-4922-b121-6fcf44c27529)
Triggered alerts confirming successful detection of simulated SSH brute-force activity and validating the effectiveness of the alerting logic.

---

### 08 — SOC Authentication Monitoring Dashboard
![dashboard](https://github.com/user-attachments/assets/991c0590-eb76-464c-9fc1-78aa8d46c7b3)

A SOC-style dashboard visualizing SSH authentication failures and potential attack sources to support security monitoring and triage.

---

## Security Note
All IP addresses, hostnames, and credentials shown in this repository belong to an isolated lab environment created strictly for educational purposes.
