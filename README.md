# Multi-Agent System for Smart Kitchen Renovation

A collaborative **AI-powered multi-agent system** built using **Google Vertex AI**, **ADK**, **AlloyDB**, **MCP Toolbox**, and **Gemini 2.5**, designed to automate the process of kitchen renovation through intelligent agents.

> 🧠 Built as part of **Code Vipassana Season 10** organized by **GDG Cloud Kochi**

---

## 🧩 Project Overview

This project simulates a smart kitchen renovation workflow with **three autonomous agents**, coordinated by a **Root Agent**:

1. **📄 Renovation Proposal Agent**  
   - Generates a kitchen renovation proposal document based on the user's specifications.  
   - Uploads the generated PDF to a **Google Cloud Storage** bucket.

2. **✅ Permits & Compliance Check Agent**  
   - Validates renovation plans against local regulations.  
   - Creates checklists and drafts official emails for authorities.

3. **📦 Order Status Check Agent**  
   - Retrieves order status from an **AlloyDB** procurement database.  
   - Built using **MCP Toolbox** and **Cloud Run Functions**.

---

## ⚙️ Technologies Used

- [Vertex AI](https://en.wikipedia.org/wiki/Vertex_AI)
- [Gemini 2.5](https://en.wikipedia.org/wiki/Gemini_(language_model))
- [Google ADK](https://cloud.google.com/vertex-ai/docs/agents/overview)
- [MCP Toolbox](https://github.com/GoogleCloudPlatform/mcp-toolbox)
- [AlloyDB](https://cloud.google.com/alloydb)
- [Google Cloud Functions](https://cloud.google.com/functions)
- [Google Cloud Storage](https://cloud.google.com/storage)
- Python, Java (Cloud Function)
- LangChain Toolbox

---

## 🚀 How to Run

### CLI
```bash
adk run .
```

### Web UI (ADK Provisioned)
```bash
adk web
```

Ensure your environment variables and credentials are configured (use a `.env` file with necessary keys and bucket details).

---

## 🧠 Agent Architecture

```
Root Agent
│
├── Renovation Proposal Agent (PDF creation + GCS upload)
├── Permits and Compliance Agent (Permits checklist + email)
└── Order Status Agent (AlloyDB + MCP Toolbox integration)
```

---

## 🖼️ Result Screenshots
### 1. Renovation proposal agent output
![Session_1_Result](https://github.com/user-attachments/assets/9d55c4b4-bf16-4a8d-9f86-5eb6b128585d)
![sess1_result_b](https://github.com/user-attachments/assets/45685fcf-8b35-4412-9590-77c681677b91)
![sess1_result_c](https://github.com/user-attachments/assets/72550f53-1f04-4ff6-8c39-0634f89fc997)

### 2. Proposal PDF uploaded in Cloud Storage bucket
![Storage_Bucket_for_renovation_agent](https://github.com/user-attachments/assets/572a9d72-bdcf-4ef2-ba58-3c3ef83e0829)


### 3. Root agent web UI output
![Session_2_Result](https://github.com/user-attachments/assets/02d0fb32-1237-4401-b2b7-27edaf8a6e6f)

### 4. Procurement order status agent output 
![Session_3_Result](https://github.com/user-attachments/assets/5b3fbf18-eae0-49b7-81a3-09f5bd9679f7)

### 5. AlloyDB table for procurement material order status
![Sess_3_AlloyDB_table](https://github.com/user-attachments/assets/2de3dd55-e645-4927-986e-816c165c5836)


---

## 📂 Project Structure

```
.
├── agent.py                   # Root agent + sub-agents
├── mcp-toolbox/              
│   ├── mcp_agent.py          # MCP agent logic
│   └── tools.yaml            # AlloyDB connection config
├── Cloud_Run_Function/
│   ├── ProposalOrdersTool.java # Cloud Function for order status
│   └── pom.xml
├── database_script.sql       # DDL + sample inserts for AlloyDB
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Author

Built with ❤️ by **Fathima Zulaikha** during **Code Vipassana S10**  
👉 Organized by [GDG Cloud Kochi](https://gdg.community.dev/gdg-cloud-kochi/)

---
