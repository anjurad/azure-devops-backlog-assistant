# Azure DevOps Backlog Assistant – Optimised Prompt

This repository contains an **optimised prompt** for ChatGPT or GitHub Copilot to act as an **experienced Business Analyst and CSV generator**.  

- Produces **Epics → Features → User Stories → Tasks** using Agile best practice (INVEST, DoR/DoD).  
- Outputs **ADO-compatible CSVs** for both initial import and iterative updates.  
- Acts as an **educator**: explains story-writing best practice, enforces acceptance criteria, and helps users improve backlog quality.  
- Supports **iteration loop**: download → review CSV → safe updates → re-upload.  

---

## 📋 Usage Instructions

### 1. Copy Prompt
Copy the full prompt (below) into ChatGPT or GitHub Copilot instructions.  
Then provide your backlog requirements (e.g., “Set up runbooks, Terraform modules, certifications”).  

### 2. Generate Backlog
The assistant will:  
- Ask clarifying questions.  
- Draft backlog items (Epics → Tasks).  
- Produce an ADO-compatible CSV.

### 3. Import to ADO
- Go to **Boards → Queries → Import Work Items**.  
- Import the CSV.  
- For initial import: omit `ID`.  
- For updates: include `ID`.  
- For hierarchy: use `Title 1`, `Title 2`, etc.  

### 4. Iterate
- Export CSV from ADO.  
- Ask the assistant to review/update it.  
- Re-import updated CSV.

---

## 🧑‍💼 Final Optimised Prompt

See `FULL_PROMPT.md` for the full optimised prompt and examples.

---

## 📚 Many-Shot Examples Included
- **Epic 1:** Standardised Artefacts (HLD/LLD templates).  
- **Epic 2:** Reusable Terraform Modules.  
- **Epic 3:** Customer Runbooks.  
- **Epic 4:** Team Certifications.  
- **Epic 5:** Sales Decks.  

These are pre-populated as working examples.

---

## ✅ Next Steps
- Extend backlog items for your practice setup.  
- Use `sample-backlog.csv` as a seed import to test.  
- Keep completed CSVs versioned in this repo for traceability.  


---

## 📄 Full Prompt File
See [FULL_PROMPT.md](FULL_PROMPT.md) for the **complete optimised prompt** with examples.
