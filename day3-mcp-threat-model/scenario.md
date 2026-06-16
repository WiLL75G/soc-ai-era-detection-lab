# MCP Threat Model Scenario Definition

## System Under Assessment
An enterprise AI coding assistant connected via the Model Context
Protocol (MCP) to four external systems used daily by development teams.

## Connected Systems (MCP Servers)
1. **GitHub** source code repository access (read/write)
2. **Jira** ticket management and issue tracking (read/write)
3. **Slack** team communication (read/write)
4. **Secrets Manager** internal credential storage (read access)

## Agent Capabilities
- Reads code from GitHub repositories
- Creates and modifies pull requests
- Reads and updates Jira tickets based on developer requests
- Posts messages and reads channel history in Slack
- Retrieves credentials from the secrets manager when a task requires them

## User Base
All developers in the engineering organisation interact with the agent
daily through a chat interface integrated into their IDE.

## Trust Boundaries
- Developer to Agent: trusted internal users, unauthenticated intent
- Agent to MCP Servers: agent holds standing credentials for all four systems
- External Content to Agent: GitHub issues, Jira tickets, and Slack messages
  can be authored by anyone with access to those platforms, including
  external contributors and lower-trust accounts

## Why This Scenario Matters
This configuration is common in 2026 enterprise environments. The agent's
broad access combined with its exposure to untrusted external content
(tickets, issues, messages) creates a wide attack surface that traditional
threat modelling frameworks were not designed to address.