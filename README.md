
## 🧠 Knowledge Decay Tracker

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3.2-lightgrey?logo=flask&logoColor=black)
![Hackathon](https://img.shields.io/badge/Hackathon-SuperHack%202025-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github&logoColor=white)

---

## 📌 Project Overview
The **Knowledge Decay Tracker** is a prototype application designed to help **MSP (Managed Service Provider) and IT teams track the retention of knowledge within the team over time**.  
It highlights areas where team members may need refresher sessions or training, ensuring that critical knowledge is retained and applied effectively.  

This tool is especially useful for:
- IT teams maintaining operational knowledge  
- MSP teams tracking client-specific knowledge  
- Teams who want to minimize skill gaps over time  

---

## 🛠 Key Features
- Track knowledge retention for multiple topics or technical areas  
- Monitor when refresher sessions are required  
- Easy-to-use frontend interface for team interaction  
- Modular backend powered by Flask  

---

## 💻 Tech Stack
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, Flask  
- **Data Storage:** CSV / Local files  

---
 
## 🚀 How to Run Locally (Windows)

Follow these steps to run the Knowledge Decay Tracker on your local machine:

1. **Clone the repository-**
git clone https://github.com/VegiHarshitha58/Knowledge-Decay-Tracker.git

      By doing this, you will get the project folder in your system.


2. **Navigate to the backend folder-**
open the command prompt add the path of the backend folder like below,

  cd Knowledge-Decay-Tracker/backend


3. **Create a virtual environment (optional but recommended)-**
python -m venv venv

  By using the above code, you can create virtual environment


4. **Activate the virtual environment-**
 On Windows Command Prompt:

  venv\Scripts\activate

  On Windows PowerShell:

  .\venv\Scripts\Activate.ps1

   You should see (venv) appear in your terminal prompt, indicating the virtual environment is active.



5. **Install required dependencies-**
  pip install flask

  This installs flask which is used for running the backend


6. **Run the backend-**
python app.py

You should see a message like:

Running on http://127.0.0.1:5000

By clicking you can see how backend works for this tool.


7. **Open the frontend-**
Go to the frontend folder: Knowledge-Decay-Tracker/frontend

Open index.html in your browser

Or use VS Code Live Server for a live reload experience

This shows the exact website of the knowledge decay tracker.

8. **Interact with the app-**
Add/view knowledge items,

Monitor retention and decay across your team


---

## 📁 Folder Structure
Knowledge-Decay-Tracker/
│
├── backend/
│    └── app.py,data.json
│
├── frontend/
│    └── index.html
│
└── README.md

---

 ## 📝 Usage Instructions

 -Add technical knowledge items or tasks to track.

 -Monitor retention over time across team members.

 -Update data regularly to maintain accuracy and prevent knowledge gaps.

---

## ⚡ Notes

 -Prototype developed for Hack2Skill SuperHack 2025.

 -Backend runs locally using Flask.

 -Frontend can be opened directly in the browser.

 -Full deployment requires a live hosting solution.

---

## 🎯 Future Enhancements

 -Add user authentication for multiple team members

 -Integrate a database for scalable storage and analytics

 -Deploy a live web version accessible online for team-wide use
