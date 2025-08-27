# Azure DevOps Backlog Assistant (MCP-enabled)

A GitHub Copilot Agent Mode prompt package that helps create, query, and manage Azure DevOps Boards work items using the Model Context Protocol (MCP) server tooling.

This repository contains an MCP-enabled prompt and guidance for working with Azure Boards programmatically through an MCP server integration. It is intended for Business Analysts, Product Owners, and engineers who want to automate backlog creation, enforce backlog quality, and use structured YAML payloads when interacting with the MCP server.

## Table of Contents

- [What this project is](#what-this-project-is)
- [Prerequisites and Setup](#prerequisites-and-setup)
- [Key Features](#key-features)
- [How to Use](#how-to-use)
- [Files in this Repository](#files-in-this-repository)
- [Work-in-Progress (wip) Folder](#work-in-progress-wip-folder)
- [Recommendations for Maintainers](#recommendations-for-maintainers)
- [Contributing](#contributing)

## What this project is

- A curated set of prompt instructions and helper examples for an agent that integrates with an Azure DevOps MCP server.
- Example YAML payloads that show how to create Epics, Features, Stories, Tasks and link them.
- Best-practice guidance baked into the prompt for backlog grooming, acceptance criteria, DoD, and sizing advice.

## Prerequisites and Setup

This project requires integration with VS Code, GitHub Copilot, and the Azure DevOps MCP Server. Follow these steps to set up your environment.

### Prerequisites
- Install [VS Code](https://code.visualstudio.com/download) or [VS Code Insiders](https://code.visualstudio.com/insiders).
- Install [Node.js](https://nodejs.org/en/download) version 20 or higher.
- Install [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli).
- Log in to Azure via the CLI: `az login`.
- Ensure the GitHub Copilot and Copilot Chat extensions are installed (extension IDs: `GitHub.copilot`, `GitHub.copilot-chat`).

### VS Code and GitHub Copilot Configuration
This project includes a committed workspace settings file (`.vscode/settings.json`) to enable and standardize GitHub Copilot and Copilot Chat behavior for contributors. The workspace settings include:

- `github.copilot.enable`
- `github.copilot.chat.enable`
- `github.copilot.chat.todoList.enabled`
- `github.copilot.chat.todoList.openOnStart`
- `github.copilot.chat.edits.suggestRelatedFilesFromGitHistory`
- `github.copilot.chat.edits.suggestRelatedFilesForTests`
- `github.copilot.chat.agent.maxRequests`
- `github.copilot.chat.agent.maxConcurrentRequests`
- `github.copilot.chat.agent.conversationHistoryEnabled`
- `github.copilot.chat.agent.maxConversationLength`
- `github.copilot.chat.suggestions.enabled`
- `editor.inlineSuggest.enabled`
- `notebook.defaultFormatter` (set to `GitHub.copilot`)
- `git.autofetch`
- `chat.mcp.serverSampling` (MCP sampling for allowed models)

**Notes**:
- The workspace file is intended to make behavior reproducible for collaborators. Users can still override values via their User settings.
- If you want any wording changed or additional instructions (e.g., how to revert individual keys or recommended extension versions), tell me what to add.

### Azure DevOps MCP Integration
This project is designed to work with the [Azure DevOps MCP Server](https://github.com/microsoft/azure-devops-mcp), a Model Context Protocol (MCP) server that brings Azure DevOps context directly to your agents in editors like VS Code.

#### Overview
The Azure DevOps MCP Server enables you to perform a wide range of Azure DevOps tasks directly from your code editor, such as:
- Listing projects, teams, and work items.
- Creating and updating work items (e.g., Epics, Features, Stories, Tasks).
- Managing repositories, pull requests, builds, releases, and wikis.
- Searching code, work items, and wiki pages.

It provides a thin abstraction layer over Azure DevOps REST APIs, making data access straightforward while letting the language model handle complex reasoning.

#### Setup Summary in VS Code
To integrate the Azure DevOps MCP Server with VS Code and GitHub Copilot:

1. **Installation**:
   - **One-Click Install (Recommended)**: Use the [one-click install link](https://insiders.vscode.dev/redirect/mcp/install?name=ado&config=%7B%20%22type%22%3A%20%22stdio%22%2C%20%22command%22%3A%20%22npx%22%2C%20%22args%22%3A%20%5B%22-y%22%2C%20%22%40azure-devops%2Fmcp%22%2C%20%22%24%7Binput%3Aado_org%7D%22%5D%7D&inputs=%5B%7B%22id%22%3A%20%22ado_org%22%2C%20%22type%22%3A%20%22promptString%22%2C%20%22description%22%3A%20%22Azure%20DevOps%20organization%20name%20%20%28e.g.%20'contoso'%29%22%7D%5D) in VS Code. After installation, select GitHub Copilot Agent Mode and refresh the tools list.
   - **Manual Install**: Create a `.vscode/mcp.json` file in your project with the following content:
     ```json
     {
       "inputs": [
         {
           "id": "ado_org",
           "type": "promptString",
           "description": "Azure DevOps organization name (e.g. 'contoso')"
         }
       ],
       "servers": {
         "ado": {
           "type": "stdio",
           "command": "npx",
           "args": ["-y", "@azure-devops/mcp", "${input:ado_org}"]
         }
       }
     }
     ```
     Save the file, then click 'Start' in VS Code.

2. **Enable and Use**:
   - Open GitHub Copilot Chat and switch to [Agent Mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode).
   - Click "Select Tools" and choose the available Azure DevOps tools.
   - Try prompts like "List ADO projects" or "List my work items for project 'Contoso'".

3. **Enhancements**:
   - Create a `.github/copilot-instructions.md` file in your project and include: "This project uses Azure DevOps. Always check to see if the Azure DevOps MCP server has a tool relevant to the user's request."
   - Use domains (e.g., add `-d core work work-items` to args) to load only specific tool groups and avoid overwhelming the model.

For full details, including troubleshooting, examples, and usage with other tools (e.g., Visual Studio 2022, Claude Code, Cursor), refer to the [Getting Started documentation](https://github.com/microsoft/azure-devops-mcp/blob/main/docs/GETTINGSTARTED.md).

### Quick Start Checklist
1. Install prerequisites (VS Code, Node.js, Azure CLI).
2. Configure VS Code and enable GitHub Copilot extensions.
3. Set up the Azure DevOps MCP Server using one-click or manual install.
4. Switch to GitHub Copilot Agent Mode and select Azure DevOps tools.
5. Start using the project examples!

## Key features

- Standards enforcement: requires acceptance criteria and Definition of Done for every story.
- Hierarchy support: Epic → Feature → Story → Task with sample YAML payloads ready to send to the MCP server.
- Educates: contains examples and guidance for writing INVEST-compliant user stories and splitting large stories.

## Files in this Repository

### Core Documentation
- `README.md` — This file. Contains project overview, setup instructions, usage examples, and repository structure.
- `CONTRIBUTING.md` — Guidelines for contributing to the project, including development setup and contribution process.
- `LICENSE` — Project license information.

### MCP Integration & Prompts
- `.github/copilot-instructions.md` — The core agent prompt and MCP examples. Contains detailed behavioral rules, YAML payload templates, and best practices for Azure DevOps work item management.
- `.vscode/settings.json` — Workspace settings for VS Code and GitHub Copilot configuration to ensure consistent behavior across contributors.

### Configuration Files
- `.gitignore` — Git ignore rules, including special handling for the wip folder.
- `.vscode/mcp.json` — MCP server configuration (created during setup).

> **Note**: The project focuses on prompt materials and documentation rather than runnable code. It serves as a template for building Azure DevOps MCP integrations and provides comprehensive guidance for backlog management automation.

## How to Use

Once your environment is set up (see [Prerequisites and Setup](#prerequisites-and-setup)), follow these steps:

1. Open `.github/copilot-instructions.md` to review the agent prompt and examples.
2. Use your MCP-enabled agent (e.g., GitHub Copilot Agent Mode with Azure DevOps MCP Server) and paste or reference these YAML examples when creating work items.
3. Confirm changes before the agent executes them—the agent's flow includes a confirmation step before creating/updating real work items.

### Example: Create an Epic (MCP YAML Payload)

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

## Work-in-Progress (wip) Folder

The `./wip` directory is used for transient files that are not yet ready for mainline commits. This includes:

- Drafts, scratch notes, and working copies of documentation.
- Any other files that are experimental or in development.

> **Note**: Files in this directory represent ongoing work product related to Azure DevOps backlog management, MCP integration testing, and project development. These are temporary artifacts that may include experimental YAML payloads, test data exports, or documentation drafts that are not yet ready for the main repository.

### Rules for the wip Folder
- The entire `./wip` directory is ignored by Git by default to keep the repository root clean.
- However, `wip/README.md` is explicitly tracked (negated in `.gitignore`) to document the folder's purpose.
- To temporarily track other files in `wip/`, add a negation in `.gitignore` (e.g., `!/wip/filename`) or use `git add -f wip/filename`.
- When files are ready, move them to the appropriate location in the repository and remove from `wip/`.

See `wip/README.md` for more details on usage.

## Recommendations for maintainers

- Add a LICENSE to the repository (MIT or similar) if you plan to share this publicly.
- Add a `CONTRIBUTING.md` describing how to propose changes to the prompt and examples.
- If you build tooling around the prompt, include small CLI helpers and a `package.json` or `requirements.txt` depending on language.

## Contributing

Please open issues or pull requests. If this becomes a collaborative project, add a contribution guide and code of conduct.

