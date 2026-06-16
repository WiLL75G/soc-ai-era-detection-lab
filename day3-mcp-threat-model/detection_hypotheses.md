# MCP Agent Detection Hypotheses

## Purpose
Each hypothesis below translates a STRIDE threat from stride_threat_model.md
into a concrete, testable detection rule a SOC analyst could implement in
a SIEM, even without a pre-built signature for this attack class.

## Hypothesis 1 Unusual Agent Commit Volume
**Threat addressed:** Tampering / Elevation of Privilege
**Detection logic:** If the AI agent makes more than 10 code commits within
a 5 minute window, raise an alert.
**Rationale:** Normal developer-reviewed agent usage produces a slower,
deliberate commit cadence. A burst of rapid commits suggests the agent
is acting on injected instructions rather than a single developer task.

## Hypothesis 2 Secrets Manager Access Outside Business Hours
**Threat addressed:** Information Disclosure
**Detection logic:** If the agent's service account accesses the secrets
manager outside 08:00 to 18:00 local time, raise an alert.
**Rationale:** While AI agents do not need business-hour boundaries
the way humans do, access to high-sensitivity systems like a secrets
manager occurring outside reviewed working hours increases the likelihood
the action was triggered by injected content rather than a legitimate
developer request.

## Hypothesis 3 Tool Description Length Anomaly
**Threat addressed:** Tampering (Tool Poisoning)
**Detection logic:** If any MCP tool description exceeds 500 characters,
flag it for manual security review before the agent is permitted to use it.
**Rationale:** Legitimate tool descriptions are concise and functional.
Tool poisoning attacks require verbose hidden instructions embedded in
metadata, making description length a simple but effective tripwire.

## Hypothesis 4 Agent Action Following External Content Read
**Threat addressed:** Information Disclosure / Elevation of Privilege
**Detection logic:** If the agent reads a Jira ticket or GitHub issue and
then, within the same session, calls the secrets manager or Slack post
tool, flag the session for review.
**Rationale:** This sequence read untrusted content, then immediately
take a sensitive action is the behavioural signature of indirect
prompt injection succeeding. The threat is not the content itself but
the action that follows it.

## Hypothesis 5 Cross-System Action Outside Task Scope
**Threat addressed:** Elevation of Privilege
**Detection logic:** If the agent's actions in a single session span more
than 2 of the 4 connected systems (GitHub, Jira, Slack, Secrets Manager),
flag for review.
**Rationale:** Most legitimate developer tasks involve 1 to 2 systems
at most. An agent touching 3 or more systems in one session suggests
either a misunderstood task or a compromised reasoning chain following
injected instructions.

## Why These Hypotheses Matter
None of these require a vendor signature or a known CVE. Each is built
from first-principles reasoning about how a legitimate agent should
behave versus how a compromised one would behave. This is exactly the
skill gap most cybersecurity professionals have not yet closed and
exactly what makes agentic threat modelling valuable in 2026.