# MCP Threat Model Scenario Definition

One AI agent, four connected systems, and a trust boundary most reviews miss: the agent reads content anyone can author. This is the system the STRIDE threat model assesses, and the scenario is deliberately realistic, a configuration common in 2026 enterprises, not a contrived worst case.

## System Under Assessment

An enterprise AI coding assistant connected via the Model Context Protocol (MCP) to four external systems used daily by development teams.

## Connected Systems (MCP Servers)

1. **GitHub** — source code repository access (read/write)
2. **Jira** — ticket management and issue tracking (read/write)
3. **Slack** — team communication (read/write)
4. **Secrets Manager** — internal credential storage (read access)

The access levels matter to the analysis. Three systems are read/write; the secrets manager is read-only, a deliberate least-privilege choice. Read-only is not safe, though, reading a credential is all an attacker needs to exfiltrate it. The scope reduction limits what can be *changed*, not what can be *stolen*.

## Agent Capabilities

- Reads code from GitHub repositories
- Creates and modifies pull requests
- Reads and updates Jira tickets based on developer requests
- Posts messages and reads channel history in Slack
- Retrieves credentials from the secrets manager when a task requires them

## User Base

All developers in the engineering organisation interact with the agent daily through a chat interface integrated into their IDE. Daily, organisation-wide use means the agent is high-value and always-on, a compromise is not a rare edge case, it is a standing exposure.

## Trust Boundaries

- **Developer to Agent:** trusted internal users, unauthenticated intent
- **Agent to MCP Servers:** the agent holds standing credentials for all four systems
- **External Content to Agent:** GitHub issues, Jira tickets, and Slack messages can be authored by anyone with access to those platforms, including external contributors and lower-trust accounts

The third boundary is the one that breaks conventional threat modelling. A traditional app trusts its inputs because developers define them. This agent consumes content authored by people the organisation does not fully trust, and treats it as instruction-bearing, which means the attack surface is not the chat box, it is every ticket, issue, and message the agent will ever read.

## Why This Scenario Matters

This configuration is common in 2026 enterprise environments. The agent's broad access, combined with its exposure to untrusted external content (tickets, issues, messages), creates a wide attack surface that traditional threat-modelling frameworks were not designed to address. Defining the scenario precisely, exactly what the agent can touch and exactly whose content it trusts, is what makes the STRIDE analysis that follows concrete rather than abstract. A threat model is only as good as the boundaries it starts from.
