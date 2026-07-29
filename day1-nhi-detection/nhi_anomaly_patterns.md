# NHI Anomaly Patterns SOC Detection Reference

Five behavioural signals that separate a compromised non-human identity from a normally-operating one. None of them depend on a failed login, because a compromised NHI has valid credentials and never fails one. Each pattern is a deviation from the identity's known-good baseline, and the fifth is what turns four weak signals into one strong verdict.

## What is a Non-Human Identity (NHI)?

Service accounts, API keys, and AI agent identities that operate autonomously inside enterprise environments without human oversight. They behave like software: predictable, scheduled, scoped, which is exactly what makes deviation detectable once you have baselined normal.

## The 5 Anomaly Patterns Used in This Detection

### Pattern 1 — Login from Unknown External IP

Normal NHI behaviour operates from internal IP ranges (e.g. 10.0.x.x). An external IP such as `185.220.101.34` indicates potential compromise or credential theft. A service account has no reason to appear from outside the network; when it does, the credential is somewhere it should not be.

### Pattern 2 — Activity Outside Business Hours

Service accounts follow predictable schedules. Activity between 01:00 and 04:00 with no change-management record is a strong indicator of unauthorised access. The absence of a change ticket is as much the signal as the hour itself, legitimate off-hours automation is planned and documented.

### Pattern 3 — Bulk Data Access

Normal API calls access small record sets (1–50 records). Accessing 800–2000 records in a single session indicates data staging for exfiltration. The volume is the tell: a jump of one to two orders of magnitude over baseline is not a busy day, it is someone taking everything before they lose access.

### Pattern 4 — Access to Admin Endpoints

Standard service-account scope does not include `/api/v1/admin/export`. Access to admin endpoints outside a defined role scope signals privilege misuse or lateral movement. This is where over-permissioning turns from a latent risk into an active one, the account could always reach the endpoint, and now it has.

### Pattern 5 — Consistent Account Under All Anomalies

All four patterns occurring under the same account (`svc_ai_agent_01`) simultaneously is high-confidence confirmation of compromise. This is the pattern that matters most. Any single anomaly could be a misconfiguration or a benign edge case; all four converging on one identity in one session is not coincidence, it is an incident. Detection is the convergence, not any one flag.

## How to Use This Reference

These five patterns are the behavioural baseline a SOC tunes against. Patterns 1–4 are individually noisy and will produce false positives on their own, which is expected. Pattern 5, the convergence, is what a production rule should weight most heavily, because it is the one that separates a real compromise from four unrelated quirks. Alert loudly on convergence; treat single patterns as enrichment, not escalation.
