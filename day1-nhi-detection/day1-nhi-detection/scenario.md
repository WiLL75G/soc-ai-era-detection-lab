# NHI Anomaly Detection Scenario Definition

## System Under Assessment
An enterprise environment where AI agents and automated service accounts
operate alongside human employees, each holding valid credentials and
API access to internal systems.

## Compromised Entity
**svc_ai_agent_01** an AI service account with standing access to
internal API endpoints, including an administrative data export endpoint.

## Normal Behaviour Baseline
- Operates from internal IP range: 10.0.1.45 to 10.0.1.47
- Accesses standard endpoints: /api/v1/users and /api/v1/billing
- Retrieves 1 to 50 records per session
- Active during business hours with no fixed schedule restrictions
  enforced at the network layer

## Attack Scenario
The service account's credentials are compromised through leaked
secrets, an exposed API key, or a supply chain compromise. The attacker
uses the valid credentials to access the account from an external IP,
during off-hours, targeting the administrative export endpoint to
exfiltrate customer records in bulk.

## Trust Boundaries
- Service Account to API: standing trust based on valid credentials only,
  no additional behavioural verification
- API to Data Store: full read access scoped to the service account's
  assigned role, which includes the admin export endpoint
- Network Perimeter to Internal Systems: no IP allowlisting enforced
  for this service account

## Why This Scenario Matters
Non-Human Identities now outnumber human employees in most enterprises.
They produce no failed login attempts when compromised because the
credentials used are valid. Traditional perimeter and authentication-based
detection does not catch this. Only behavioural baselining knowing what
normal access looks like can surface the anomaly.