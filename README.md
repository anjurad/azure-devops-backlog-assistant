# Azure DevOps Backlog Assistant (MCP-enabled)

A GitHub Copilot Agent Mode prompt package that helps create, query, and manage Azure DevOps Boards work items using the Model Context Protocol (MCP) server tooling.

This repository contains an MCP-enabled prompt and guidance for working with Azure Boards programmatically through an MCP server integration. It is intended for Business Analysts, Product Owners, and engineers who want to automate backlog creation, enforce backlog quality, and use structured YAML payloads when interacting with the MCP server.

## What this project is

- A curated set of prompt instructions and helper examples for an agent that integrates with an Azure DevOps MCP server.
- Example YAML payloads that show how to create Epics, Features, Stories, Tasks and link them.
- Best-practice guidance baked into the prompt for backlog grooming, acceptance criteria, DoD, and sizing advice.

## Key features

- Standards enforcement: requires acceptance criteria and Definition of Done for every story.
- Hierarchy support: Epic → Feature → Story → Task with sample YAML payloads ready to send to the MCP server.
- Educates: contains examples and guidance for writing INVEST-compliant user stories and splitting large stories.

## Files in this repository

- `epics.md` — Example or starter epics (project content may vary).
- `.github/copilot-instructions.md` — The core agent prompt and MCP examples. This file contains the detailed MCP examples and behavioural rules used by the agent.

> Note: The project currently contains only prompt materials and documentation. It does not include a runnable MCP server or scripts to call the MCP endpoints. Use this repo as a prompt template and reference for building automation around Azure DevOps MCP tools.

## How to use

1. Open `.github/copilot-instructions.md` to review the agent prompt and examples.
2. Use your MCP-enabled agent (for example, the GitHub Copilot Agent Mode connected to an Azure DevOps MCP Server) and paste or reference these YAML examples when creating work items.
3. Confirm changes before the agent executes them — the agent’s flow includes a confirmation step before creating/updating real work items.

### Example: create an Epic (MCP YAML payload)

Use the `mcp_ado_wit_create_work_item` tool with the following YAML-like payload as the body:

```yaml
#mcp wit_create_work_item
type: Epic
title: Architecture & Design Artefacts
description: "<p>Establish consistent, audit-ready design documentation to accelerate delivery and ensure governance across engagements.</p>"
acceptance_criteria: "<ul><li>Given a new engagement, when a consultant produces a design, then standard templates are used.</li><li>Given customer review, when artefacts are handed over, then they align with Microsoft best practices.</li></ul>"
tags: ["design", "governance"]
```

The `.github/copilot-instructions.md` file contains additional examples for Features, Stories, Tasks, and runbook items.

## Recommendations for maintainers

- Add a LICENSE to the repository (MIT or similar) if you plan to share this publicly.
- Add a `CONTRIBUTING.md` describing how to propose changes to the prompt and examples.
- If you build tooling around the prompt, include small CLI helpers and a `package.json` or `requirements.txt` depending on language.

## Contributing

Please open issues or pull requests. If this becomes a collaborative project, add a contribution guide and code of conduct.

