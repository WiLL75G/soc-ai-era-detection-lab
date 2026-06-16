# NHI Anomaly Patterns SOC Detection Reference

## What is a Non-Human Identity (NHI)?
Service accounts, API keys, and AI agent identities that operate
autonomously inside enterprise environments without human oversight.

## The 5 Anomaly Patterns Used in This Detection

### Pattern 1 Login from Unknown External IP
Normal NHI behaviour operates from internal IP ranges (e.g. 10.0.x.x).
An external IP such as 185.220.101.34 indicates potential compromise
or credential theft.

### Pattern 2 Activity Outside Business Hours
Service accounts follow predictable schedules.
Activity between 01:00–04:00 with no change management record
is a strong indicator of unauthorised access.

### Pattern 3 Bulk Data Access
Normal API calls access small record sets (1–50 records).
Accessing 800–2000 records in a single session indicates
data staging for exfiltration.

### Pattern 4 Access to Admin Endpoints
Standard service account scope does not include /api/v1/admin/export.
Access to admin endpoints outside defined role scope signals
privilege misuse or lateral movement.

### Pattern 5 Consistent Account Under All Anomalies
All 4 patterns occurring under the same account (svc_ai_agent_01)
simultaneously is high-confidence confirmation of compromise.
