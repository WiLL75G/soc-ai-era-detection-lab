# MCP Agent Detection Hypotheses

Five detection rules, none needing a vendor signature or a known CVE. Each one is reasoned from first principles, how a legitimate agent behaves versus how a compromised one would, and each maps back to a specific STRIDE threat from the threat model. This is detection built for an attack class that has no pre-built signature yet, which is the whole point.

## Purpose

Each hypothesis below translates a STRIDE threat from `stride_threat_model.md` into a concrete, testable detection rule a SOC analyst could implement in a SIEM, even without a pre-built signature for this attack class.

## Hypothesis 1 — Unusual Agent Commit Volume

**Threat addressed:** Tampering / Elevation of Privilege
**Detection logic:** If the AI agent makes more than 10 code commits within a 5-minute window, raise an alert.
**Rationale:** Normal developer-reviewed agent usage produces a slower, deliberate commit cadence. A burst of rapid commits suggests the agent is acting on injected instructions rather than a single developer task, machine speed applied to an action that should move at human review pace.

## Hypothesis 2 — Secrets Manager Access Outside Business Hours

**Threat addressed:** Information Disclosure
**Detection logic:** If the agent's service account accesses the secrets manager outside 08:00 to 18:00 local time, raise an alert.
**Rationale:** AI agents do not need business-hour boundaries the way humans do, but access to a high-sensitivity system like a secrets manager outside reviewed working hours raises the likelihood the action was triggered by injected content rather than a legitimate developer request. The hour is not the crime, it is the correlation with an unreviewed trigger.

## Hypothesis 3 — Tool Description Length Anomaly

**Threat addressed:** Tampering (Tool Poisoning)
**Detection logic:** If any MCP tool description exceeds 500 characters, flag it for manual security review before the agent is permitted to use it.
**Rationale:** Legitimate tool descriptions are concise and functional. Tool poisoning attacks require verbose hidden instructions embedded in metadata, making description length a simple but effective tripwire, a crude signal that catches an attack most teams do not yet know to look for.

## Hypothesis 4 — Agent Action Following External Content Read

**Threat addressed:** Information Disclosure / Elevation of Privilege
**Detection logic:** If the agent reads a Jira ticket or GitHub issue and then, within the same session, calls the secrets manager or Slack post tool, flag the session for review.
**Rationale:** This sequence, read untrusted content then immediately take a sensitive action, is the behavioural signature of indirect prompt injection succeeding. The threat is not the content itself but the action that follows it. This is the highest-value hypothesis in the set, because it detects the attack by its shape rather than its wording, which no payload rewrite can evade.

## Hypothesis 5 — Cross-System Action Outside Task Scope

**Threat addressed:** Elevation of Privilege
**Detection logic:** If the agent's actions in a single session span more than 2 of the 4 connected systems (GitHub, Jira, Slack, Secrets Manager), flag for review.
**Rationale:** Most legitimate developer tasks involve 1 to 2 systems at most. An agent touching 3 or more systems in one session suggests either a misunderstood task or a compromised reasoning chain following injected instructions. This is the direct behavioural counterpart to the threat model's root-cause finding, standing access with no per-task scope, turned into a detectable event.

## Why These Hypotheses Matter

None of these require a vendor signature or a known CVE. Each is built from first-principles reasoning about how a legitimate agent should behave versus how a compromised one would. That reasoning is the skill: anyone can deploy a signature written by someone else, but writing detections for an attack class before the signatures exist is what a SOC needs in the window between a threat emerging and the industry catching up. In 2026, for agentic systems, that window is right now.

## Note on Hypothesis Count

This reference contains five hypotheses. Hypotheses 1–3 map directly to the three highest-risk STRIDE threats and were the original deliverable; Hypotheses 4 and 5 extend coverage to the behavioural signature of indirect injection and to the standing-access root cause, and are the stronger additions. The set is presented in full because more first-principles detection coverage is the point of the exercise.
