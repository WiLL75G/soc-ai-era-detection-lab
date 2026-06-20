```
 █████╗ ██╗      ███████╗██████╗  █████╗ 
██╔══██╗██║      ██╔════╝██╔══██╗██╔══██╗
███████║██║█████╗█████╗  ██████╔╝███████║
██╔══██║██║╚════╝██╔══╝  ██╔══██╗██╔══██║
██║  ██║██║      ███████╗██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝      ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
```

[![Blue Team Notes](https://img.shields.io/badge/Blue_Team_Notes-WilliamInCyber-1F6FEB?style=flat&logo=github&logoColor=white)](https://github.com/WiLL75G)
[![Splunk](https://img.shields.io/badge/SIEM-Splunk-65A637?style=flat&logo=splunk&logoColor=white)](https://www.splunk.com)
[![OWASP LLM Top 10](https://img.shields.io/badge/OWASP-LLM_Top_10-000000?style=flat&logo=owasp&logoColor=white)](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
[![STRIDE](https://img.shields.io/badge/Threat_Model-STRIDE-E57000?style=flat)](https://en.wikipedia.org/wiki/STRIDE_model)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-C5221F?style=flat)](https://attack.mitre.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

# SOC Detection Lab: AI-Era Threat Simulation

**Status: Complete, 4 of 4 days delivered**

---

## Project Overview

A 4-day hands-on SOC detection lab simulating AI-era threats that are actively emerging in enterprise environments in 2026. Built from scratch using Splunk, Python, STRIDE threat modelling, and the OWASP Top 10 for LLM Applications as the reference framework.

This project demonstrates the full SOC analyst workflow, covering threat simulation, log ingestion, SIEM detection rule writing, threat modelling, multi-incident correlation, MITRE ATT&CK mapping, and professional incident report documentation, applied to a threat class most entry-level analysts have never touched.

---

## Why This Project Exists

AI agents, service accounts, and autonomous copilots are being deployed
across enterprise environments at scale. By 2026, non-human identities
outnumber human employees 82:1 in many organisations. Prompt injection
is ranked the number 1 risk for LLM applications by OWASP. MCP server
attacks represent an entirely new attack class with no established
detection playbook.

Most SOC teams are not prepared for this.

This lab is built to change that starting with detection.

---

## Lab Structure

| Day | Focus | Threat Simulated | Tools | Status |
|-----|-------|-----------------|-------|--------|
| Day 1 | NHI Anomaly Detection | Compromised AI service account exfiltrating 1,877 records via admin API | Python, Splunk SPL | Complete |
| Day 2 | Prompt Injection Detection | Attacker injecting override instructions into enterprise AI assistant | Python, Splunk SPL | Complete |
| Day 3 | MCP Threat Modelling | AI coding agent connected to GitHub, Jira, Slack and secrets manager | STRIDE, draw.io | Complete |
| Day 4 | Full SOC Incident Report | Combined AI-era attack chain correlating NHI abuse, prompt injection, and MCP exploitation into one kill chain | Markdown | Complete |

---

## Key Skills Demonstrated

- Synthetic log generation using Python simulating real attack patterns
- SIEM ingestion and SPL detection rule writing in Splunk Enterprise
- Behavioural baselining identifying anomalies against known-good state
- Threat modelling using STRIDE methodology applied to AI agent systems
- Translating identified threats into testable detection hypotheses
- MITRE ATT&CK mapping for AI-era attack techniques
- Correlating multiple independent detections into a single coherent
  kill chain attributed to one threat actor
- SOC Tier 1 and Tier 2 incident documentation from detection through
  multi-phase investigation and analyst response
- OWASP LLM Top 10 applied as a practical detection framework

---

## Detection Results

| Day | Log Entries | Malicious | Flagged | False Negatives |
|-----|-------------|-----------|---------|-----------------|
| Day 1 | 100 | 20 | 38 | 0 |
| Day 2 | 85 | 15 | 15 | 0 |

## Threat Modelling Coverage

| Day | Framework | Categories Assessed | Detection Hypotheses Produced |
|-----|-----------|---------------------|-------------------------------|
| Day 3 | STRIDE | 6 of 6 | 3 |

## Incident Correlation Outcome

| Day | Role in Kill Chain | Outcome |
|-----|---------------------|---------|
| Day 1 | Initial compromise successful exfiltration | 1,877 records confirmed exfiltrated |
| Day 2 | Secondary attempt credential theft via injection | Detected and flagged before success |
| Day 3 | Architectural root cause identification | Standing access with no per-task scope |
| Day 4 | Full correlation across all three phases | Single threat actor confirmed via shared IOC |

---

## Repository Structure

```
soc-ai-era-detection-lab/
├── day1-nhi-detection/
│   ├── generate_nhi_logs.py       # NHI log generation script
│   ├── nhi_anomaly_patterns.md    # 5 anomaly patterns reference
│   └── README.md                  # Day 1 incident report
├── day2-prompt-injection/
│   ├── generate_pi_logs.py        # Prompt injection log script
│   ├── pi_indicators.md           # 6 detection indicators reference
│   └── README.md                  # Day 2 incident report
├── day3-mcp-threat-model/
│   ├── scenario.md                # Enterprise MCP scenario definition
│   ├── stride_threat_model.md     # STRIDE threat model table
│   ├── detection_hypotheses.md    # 3 SOC detection hypotheses
│   └── README.md                  # Day 3 threat model report
├── day4-incident-report/
│   └── INCIDENT_REPORT.md         # Full multi-phase incident report
├── logs/
│   ├── nhi_logs.json              # Day 1 synthetic log data
│   └── pi_logs.json               # Day 2 synthetic log data
└── screenshots/                   # Evidence — all lab screenshots
```

---

## MITRE ATT&CK Coverage

| Technique | ID | Day |
|-----------|-----|-----|
| Valid Accounts | T1078 | Day 1, Day 2, Day 3, Day 4 |
| Data from Information Repositories | T1213 | Day 1 |
| Exfiltration Over Web Service | T1567 | Day 1, Day 2, Day 3, Day 4 |
| Hijack Execution Flow | T1574 | Day 2, Day 4 |
| Unsecured Credentials | T1552 | Day 2, Day 3, Day 4 |
| Data from Local System | T1005 | Day 2 |
| Phishing | T1566 | Day 3, Day 4 |
| Resource Hijacking | T1496 | Day 3 |

---

## Reference Framework

This lab is built against the
**OWASP Top 10 for LLM Applications 2025**
as the industry baseline for AI security risks.

Primary risks covered:
- LLM01 — Prompt Injection (Day 2, Day 4)
- LLM02 — Insecure Output Handling (Day 2)
- LLM06 — Excessive Agency (Day 1, Day 3, Day 4)
- LLM08 — Vector and Embedding Weaknesses (Day 3)
- LLM09 — Misinformation (Day 3)

---

## Tools and Environment

| Tool | Purpose |
|------|---------|
| Splunk Enterprise | SIEM log ingestion and detection |
| Python 3 | Synthetic log generation |
| VS Code | Development environment |
| STRIDE | Threat modelling methodology |
| draw.io | Threat model diagrams |
| OWASP LLM Top 10 | Detection reference framework |
| GitHub | Documentation and portfolio evidence |

---

## About the Author

William Gokah is a SOC analyst building toward Tier 1 and
Tier 2 remote roles at MSSPs across the UK, UAE, and Australia. This
project is part of a broader portfolio of hands-on blue team labs built
publicly under the @WilliamInCyber brand.
