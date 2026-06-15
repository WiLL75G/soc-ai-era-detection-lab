# SOC Detection Lab AI-Era Threat Simulation

**Author:** James Williams | [@WilliamInCyber](https://x.com/WilliamInCyber)
**GitHub:** [WiLL75G](https://github.com/WiLL75G)


---

## Project Overview

A 4-day hands-on SOC detection lab simulating AI-era threats that are
actively emerging in enterprise environments in 2026. Built from scratch
using Splunk, Python, and the OWASP Top 10 for LLM Applications as the
reference framework.

This project demonstrates the full SOC analyst workflow threat simulation,
log ingestion, SIEM detection rule writing, MITRE ATT&CK mapping, and
professional incident report documentation applied to a threat class
most entry-level analysts have never touched.

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

| Day | Focus | Threat Simulated | Tools |
|-----|-------|-----------------|-------|
| Day 1 | NHI Anomaly Detection | Compromised AI service account exfiltrating 1,877 records via admin API | Python, Splunk SPL |
| Day 2 | Prompt Injection Detection | Attacker injecting override instructions into enterprise AI assistant | Python, Splunk SPL |
| Day 3 | MCP Threat Modelling | AI coding agent connected to GitHub, Jira, Slack and secrets manager | STRIDE, draw.io |
| Day 4 | Full SOC Incident Report | Combined AI-era attack NHI abuse + prompt injection + MCP exploitation | Markdown |

---

## Key Skills Demonstrated

- Synthetic log generation using Python simulating real attack patterns
- SIEM ingestion and SPL detection rule writing in Splunk Enterprise
- Behavioural baselining identifying anomalies against known-good state
- Threat modelling using STRIDE methodology applied to AI agent systems
- MITRE ATT&CK mapping for AI-era attack techniques
- SOC Tier 1 incident documentation from detection through analyst response
- OWASP LLM Top 10 applied as a practical detection framework

---

## Detection Results

| Day | Log Entries | Malicious | Flagged | False Negatives |
|-----|-------------|-----------|---------|-----------------|
| Day 1 | 100 | 20 | 38 | 0 |
| Day 2 | 85 | 15 | 15 | 0 |

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
│   └── detection_hypotheses.md   # SOC detection hypotheses
├── day4-incident-report/
│   └── INCIDENT_REPORT.md         # Full SOC incident report
├── logs/
│   ├── nhi_logs.json              # Day 1 synthetic log data
│   └── pi_logs.json               # Day 2 synthetic log data
└── screenshots/                   # Evidence — all lab screenshots
```

---

## MITRE ATT&CK Coverage

| Technique | ID | Day |
|-----------|-----|-----|
| Valid Accounts | T1078 | Day 1, Day 2 |
| Data from Information Repositories | T1213 | Day 1 |
| Exfiltration Over Web Service | T1567 | Day 1, Day 2 |
| Hijack Execution Flow | T1574 | Day 2 |
| Unsecured Credentials | T1552 | Day 2 |
| Data from Local System | T1005 | Day 2 |

---

## Reference Framework

This lab is built against the
**OWASP Top 10 for LLM Applications 2025**
as the industry baseline for AI security risks.

Primary risks covered:
- LLM01 — Prompt Injection (Day 2)
- LLM02 — Insecure Output Handling (Day 2)
- LLM06 — Excessive Agency (Day 1, Day 3)
- LLM08 — Vector and Embedding Weaknesses (Day 3)
- LLM09 — Misinformation (Day 3)

---

## Tools and Environment

| Tool | Purpose |
|------|---------|
| Splunk Enterprise | SIEM log ingestion and detection |
| Python 3 | Synthetic log generation |
| VS Code | Development environment |
| draw.io | Threat model diagrams |
| OWASP LLM Top 10 | Detection reference framework |
| GitHub | Documentation and portfolio evidence |

---

## About the Author

James Williams is an aspiring SOC analyst building toward Tier 1 and
Tier 2 remote roles at MSSPs across the UK, UAE, and Australia. This
project is part of a broader portfolio of hands-on blue team labs built
publicly under the @WilliamInCyber brand.

Portfolio: [github.com/WiLL75G](https://github.com/WiLL75G)
