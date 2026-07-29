# STRIDE Threat Model MCP-Connected AI Coding Assistant

All six STRIDE categories, each populated with an MCP-specific threat, and one column the standard framework does not have: why an AI agent makes each threat worse than it would be in a traditional application. Two of the six trace back to a single root cause, which is the finding that matters.

## Reference Scenario

See [`scenario.md`](scenario.md) for the full system definition: an enterprise AI coding assistant with standing access to GitHub, Jira, Slack, and a secrets manager.

## Threat Model Table

| STRIDE Category | Threat | Attack Example | Why AI Agents Make This Worse |
|---|---|---|---|
| **Spoofing** | Attacker impersonates a trusted MCP server | A malicious actor stands up a fake MCP server that mimics the real GitHub connector and returns poisoned tool definitions | The agent has no inherent way to verify MCP server identity beyond configuration trust; once spoofed, every tool call is compromised |
| **Tampering** | Tool poisoning via malicious tool descriptions | Hidden instructions embedded inside a tool's metadata description are read and silently followed by the agent | Traditional input validation does not apply, the "input" is the tool definition itself, which the agent trusts implicitly |
| **Repudiation** | Agent actions are not logged or attributable to a human | The agent commits code changes or sends Slack messages with no clear record of which developer's request triggered it | Non-deterministic agents may take slightly different actions on similar prompts, making after-the-fact attribution difficult without strict logging |
| **Information Disclosure** | Agent leaks secrets via indirect prompt injection | A malicious Jira ticket contains hidden instructions telling the agent to retrieve and post secrets manager credentials into a public Slack channel | The agent reads untrusted external content (tickets, issues) as part of normal operation, so the attack surface includes every system the agent touches, not just direct chat input |
| **Denial of Service** | Agent enters a resource-exhausting loop | A specially crafted GitHub issue causes the agent to recursively call tools until it exhausts API rate limits or compute budget | Agentic loops with tool-calling can spiral in ways a single-shot system cannot; the agent's own autonomy becomes the vulnerability |
| **Elevation of Privilege** | Agent uses tools outside its intended role scope | The agent uses its secrets manager access to retrieve credentials for a system unrelated to the current coding task, because nothing constrains tool use to task-relevant scope | Standing credentials across all four MCP servers mean a single compromised reasoning step grants access to everything, not just the system originally targeted |

## Reading the Table

The "Why AI Agents Make This Worse" column is the part that matters. Every one of these six threats has a classical-application analogue, spoofing, tampering, DoS, and the rest are decades old. What is new is the mechanism: an agent that trusts its tool definitions implicitly, reads attacker-authored content as instruction, and acts autonomously across four systems with one set of standing credentials. STRIDE still works as a framework; the threats it surfaces just land harder on a system that reasons and acts on its own.

## Key Insight

The most dangerous threats in this model are **Information Disclosure** and **Elevation of Privilege**, and both stem from the same root cause: the agent holds broad standing access across all four systems with no per-task scope limitation, and it processes untrusted external content as part of normal operation.

This is the finding the whole exercise exists to produce. Six threats assessed independently would yield six separate remediation tickets. Tracing two of the highest-severity ones to a single design decision, standing access with no per-task scope, collapses that into one high-leverage fix: scope the credentials per task, and both threats shrink at once. That is the difference between a threat model that generates work and one that reduces it, and it is why structured modelling beats a vulnerability scan for this class of system, the scanner finds what is broken, the model finds what is broken *by design*.
