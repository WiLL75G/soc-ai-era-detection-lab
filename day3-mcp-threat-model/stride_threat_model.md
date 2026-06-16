# STRIDE Threat Model MCP-Connected AI Coding Assistant

## Reference Scenario
See scenario.md for full system definition.

## Threat Model Table

| STRIDE Category | Threat | Attack Example | Why AI Agents Make This Worse |
|---|---|---|---|
| **Spoofing** | Attacker impersonates a trusted MCP server | A malicious actor stands up a fake MCP server that mimics the real GitHub connector and returns poisoned tool definitions | The agent has no inherent way to verify MCP server identity beyond configuration trust once spoofed, every tool call is compromised |
| **Tampering** | Tool poisoning via malicious tool descriptions | Hidden instructions embedded inside a tool's metadata description are read and silently followed by the agent | Traditional input validation does not apply the "input" is the tool definition itself, which the agent trusts implicitly |
| **Repudiation** | Agent actions are not logged or attributable to a human | The agent commits code changes or sends Slack messages with no clear record of which developer's request triggered it | Non-deterministic agents may take slightly different actions on similar prompts, making after-the-fact attribution difficult without strict logging |
| **Information Disclosure** | Agent leaks secrets via indirect prompt injection | A malicious Jira ticket contains hidden instructions telling the agent to retrieve and post secrets manager credentials into a public Slack channel | The agent reads untrusted external content (tickets, issues) as part of normal operation — the attack surface includes every system the agent touches, not just direct chat input |
| **Denial of Service** | Agent enters a resource-exhausting loop | A specially crafted GitHub issue causes the agent to recursively call tools until it exhausts API rate limits or compute budget | Agentic loops with tool-calling can spiral in ways a single-shot system cannot the agent's own autonomy becomes the vulnerability |
| **Elevation of Privilege** | Agent uses tools outside its intended role scope | The agent uses its secrets manager access to retrieve credentials for a system unrelated to the current coding task, because nothing constrains tool use to task-relevant scope | Standing credentials across all four MCP servers mean a single compromised reasoning step grants access to everything, not just the system originally targeted |

## Key Insight
The most dangerous threats in this model are Information Disclosure and
Elevation of Privilege both stem from the same root cause: the agent
holds broad standing access across all four systems with no per-task
scope limitation, and it processes untrusted external content as part
of normal operation.
