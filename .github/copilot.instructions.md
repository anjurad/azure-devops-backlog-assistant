# GitHub Copilot — Instructions for Maintaining Azure DevOps Backlog Prompt

**Last updated:** {{date}}

---

## 🎯 Purpose
These instructions guide Copilot to **maintain, optimise, and extend** the Azure DevOps Backlog Assistant prompt and related artefacts.  
They ensure that all changes remain aligned with:
- Microsoft Cloud Adoption Framework (CAF) and Well-Architected Framework (WAF).  
- Azure Advanced Specialisation audit criteria (Analytics on Azure, Build AI Apps, AI Platform).  
- Internal Bytes Data Practice standards (repeatability, metadata-driven patterns, governance).  

---

## ✅ Rules for Copilot

### 1. Scope of Copilot Edits
- Only update **prompt structure, formatting, and examples**.  
- Do **not** remove analyst/educator role requirements.  
- Ensure **CSV schema consistency** with Azure DevOps import/export (Epics → Features → Stories → Tasks).  
- Preserve links between README.md → FULL_PROMPT.md → sample-backlog.csv.  
- Maintain British English spelling and grammar.  

### 2. Optimisation Guidance
- Improve **clarity**: simplify language where verbose, expand where ambiguous.  
- Ensure **educational tone** remains (prompt must guide/coach users, not just generate outputs).  
- Verify examples remain **best practice** (INVEST model, acceptance criteria, estimates).  
- Keep CSV output specifications correct:  
  - New items: no `ID`, use `Title` hierarchy.  
  - Updates: include `ID`, avoid breaking schema.  
  - Iterative updates: preserve history, only append or update safely.  

### 3. File Management
- Prompt text must live in **FULL_PROMPT.md**.  
- README.md must only include overview + reference to FULL_PROMPT.md.  
- Always keep **sample-backlog.csv** valid for ADO import.  
- When adding new examples, update both the CSV and FULL_PROMPT.md consistently.  

### 4. Cross-Referencing
- Align backlog examples with current **Service Option artefacts** (e.g. Fabric Enablement, Lakehouse Hydration, Purview Governance, Data Quality Management).  
- Cross-check Discovery Templates and Gap Analysis documents to ensure backlog items reflect **audit evidence requirements**.  

### 5. Quality & Audit Readiness
- Ensure each Epic/Story has:  
  - Acceptance criteria.  
  - Definition of Done.  
  - Estimate.  
  - Business outcome linkage.  
- If edits risk removing required audit content, flag and ask for clarification.  
- When in doubt, **add clarifying questions** in the prompt rather than assume.  

---

## ⚙️ Example Copilot Behaviours

- **Allowed:**  
  - “Reformat acceptance criteria into bullet points.”  
  - “Add an Epic for Terraform IaC based on Fabric Enablement service option.”  
  - “Update CSV sample to include a Runbook Documentation task.”  

- **Not Allowed:**  
  - “Delete analyst education responsibilities.”  
  - “Change CSV headers.”  
  - “Strip audit-related tags like (Required for Audit).”  

---

## 📌 Maintenance Checklist
When committing updates, Copilot should:
1. Validate Markdown syntax.  
2. Validate CSV schema by test-importing into Azure DevOps.  
3. Check cross-references between README.md, FULL_PROMPT.md, and CSV.  
4. Ensure examples reflect Bytes’ Service Options and Microsoft partner frameworks.  
5. Include a short changelog entry in commit message.  

---