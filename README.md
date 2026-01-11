# Python Log Analyzer for Brute-Force Detection

## Overview
This project is a beginner-friendly security engineering exercise focused on understanding how brute-force authentication attacks appear in logs and how they can be detected programmatically. The goal was not just to write Python code, but to practice thinking like a defender by turning raw log data into meaningful security signals.

---

## Why I Built This
As someone early in my cybersecurity journey, I wanted to move beyond certifications and theory and actually build something that reflects how security teams reason about attacks. Brute-force attempts are one of the most common real-world threats, and they’re also a great way to learn log analysis, detection logic, and noise reduction.

---

## What the Tool Does
- Reads authentication log entries from a file  
- Filters for failed login attempts  
- Groups failures by source IP address  
- Correlates events within a 5-minute time window  
- Flags IPs that exceed a defined failure threshold  

This mirrors how detections are designed in SIEM and security monitoring environments, just at a smaller and more approachable scale.

---

## Detection Logic
- **Threshold:** 3 failed login attempts  
- **Time Window:** 5 minutes  
- **Detection Type:** Behavior-based, time-correlated  

An IP address is flagged when multiple authentication failures occur close together in time, which helps differentiate malicious activity from normal user mistakes.

---

## MITRE ATT&CK Mapping
- **Tactic:** Credential Access  
- **Technique:** T1110 – Brute Force  

This detection aligns with MITRE ATT&CK technique T1110 by identifying repeated failed authentication attempts originating from a single source within a short time window, a common indicator of brute-force credential attacks.

---

## Technologies Used
- Python 3  
- `collections.defaultdict` for event aggregation  
- `datetime` for timestamp parsing and time-window correlation  

---

## Example Output
`Suspicious IPs detected:
192.168.1.10 → 3 failures within 5 minutes`

---

## What I Learned
- How authentication events are represented in logs  
- How attacker behavior shows up as patterns over time  
- How thresholds and time windows reduce false positives  
- How detection logic maps to real security frameworks like MITRE ATT&CK  

---

## Future Improvements
- Support for real system logs (SSH, web server logs)  
- Severity scoring based on failure volume  
- Output alerts in structured formats (JSON)  
- Mapping additional techniques beyond brute force  
