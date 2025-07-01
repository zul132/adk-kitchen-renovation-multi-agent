# Multi-Agent System for Smart Kitchen Renovation

A collaborative **AI-powered multi-agent system** built using **Google Vertex AI**, **ADK**, **AlloyDB**, **MCP Toolbox**, and **Gemini 2.5**, designed to automate the process of kitchen renovation through intelligent agents.

> 🧠 Built as part of **Code Vipassana Season 10** organized by **GDG Cloud Kochi**

[Link to my Code Vipassana Certificate](https://drive.google.com/file/d/1imIGSwtvVRrA6Fp0fcrBDdh5zCz49QLE/view?usp=sharing) 

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

| S.No | Technology | Used For |
|------|------------|----------|
| 1 | Vertex AI & [Gemini 2.5](https://deepmind.google/models/gemini/pro/) | Powers the chat-based multi-agent system for intelligent response generation and document creation. |
| 2 | [Google ADK (Agent Developer Kit)](https://google.github.io/adk-docs/) | Builds and orchestrates multi-agent workflows with sub-agent delegation and conversation management. |
| 3 | [Google Cloud Run](https://cloud.google.com/run) | Deploys the root agent and backend services in a scalable, serverless environment. |
| 4 | [MCP Toolbox for Databases](https://googleapis.github.io/genai-toolbox/getting-started/introduction/) | Connects to AlloyDB and enables secure, tool-based SQL querying for material order status. |
| 5 | [AlloyDB](https://cloud.google.com/alloydb) | Acts as the backend database for procurement and delivery tracking (`material_order_status` table). |
| 6 | [Google Cloud Functions](https://cloud.google.com/functions) | Provides serverless APIs to fetch data from AlloyDB (used by the ordering agent). |
| 7 | [Google Cloud Storage](https://cloud.google.com/storage) | Stores the generated proposal PDFs uploaded by the Proposal Agent. |
| 8 | LangChain Toolbox | Supports natural language tools and actions for enhanced agent capabilities. |
| 9 | Python | Python handles agent orchestration and logic. |
| 10 | Java | Java is used in the Cloud Function for database access. |

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

Built with ❤️ by **Fathima Zulaikha** during **Code Vipassana Season 10**  
👉 Organized by [GDG Cloud Kochi](https://gdg.community.dev/gdg-cloud-kochi/)

---
