# SSH Brute Force Detection & Alerting

## Project Overview
This project demonstrates the detection of SSH brute-force attacks by analyzing Linux authentication logs and triggering alerts when suspicious login behavior is observed. The goal is to simulate a realistic credential access attack and implement correlation-based detection using a SIEM.

The project was built as part of a security monitoring lab and focuses on log ingestion, detection engineering, alerting, and validation, core skills used in a Security Operations Center (SOC).

---

## Objectives
- Detect SSH brute-force authentication attempts
- Analyze Linux authentication logs (`/var/log/auth.log`)
- Create correlation-based SIEM detections
- Trigger alerts based on defined thresholds
- Map detections to MITRE ATT&CK techniques

---

## Tools & Technologies
- **Ubuntu Linux** (SSH Server)
- **Kali Linux** (Attack Simulation)
- **OpenSSH**
- **Splunk Enterprise (SIEM)**
- **Splunk Universal Forwarder**
- **VirtualBox (Internal Network)**

---

## Architecture
- Kali Linux simulates repeated failed SSH login attempts
- Ubuntu Linux hosts the SSH service and generates authentication logs
- Logs are forwarded to Splunk for centralized analysis
- Detection logic identifies brute-force behavior
- Alerts are triggered when thresholds are exceeded

---

## Log Source
Authentication events are collected from:
/var/log/auth.log
---
## Detection Logic
### Base Search
index=main "Failed password"
---
## Notes
This project was conducted in a **controlled lab environment** for educational purposes. All systems used private IP addressing and simulated activity only.
