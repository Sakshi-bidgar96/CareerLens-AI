✦ CareerLens AI – AI Career Intelligence & Resume Analyzer

<p align="center">
  <b>An Intelligent Platform for Resume Analysis, Job Exploration and Career Development</b>
</p>🚀 About the Project

CareerLens AI is an AI-powered career intelligence platform designed to help students and job seekers improve their career opportunities.

The platform provides resume analysis, job exploration, career guidance, knowledge graph visualization and personalized career roadmaps through an interactive and user-friendly interface.

It helps users understand their skills, explore suitable career opportunities and identify areas for professional improvement.

🎯 Problem Statement

Many students and job seekers face difficulties in:

- Creating effective resumes.
- Identifying their technical and professional skills.
- Finding suitable job opportunities.
- Understanding the skills required for specific careers.
- Planning their career development.

CareerLens AI aims to address these challenges through an intelligent and centralized career assistance platform.

✨ Key Features

1. 🔐 User Authentication

- Secure user login.
- New account registration.
- Individual user sessions.
- Personalized analysis history.

2. 📄 Resume Analyzer

- Resume analysis.
- Resume insights.
- Skill identification and evaluation.
- Helps users understand their resume strengths and improvement areas.

3. 💼 Job Explorer

- Explore job opportunities.
- Understand job-related skills.
- Explainable job matching.

4. 🧠 Knowledge Graph

- Visual representation of career-related knowledge.
- Connects skills, jobs and career information.
- Helps users understand relationships between different career concepts.

5. 🤖 Career Assistant

- AI-powered career guidance.
- Career-related assistance.
- Helps users make informed career decisions.

6. 🗺️ Career Roadmap

- Career development guidance.
- Skill improvement planning.
- Helps users identify their next career steps.

7. 📊 Dashboard & History

- Career overview dashboard.
- Previous analysis history.
- User-specific workspace.

🛠️ Technologies Used

Technology| Purpose
Python| Backend development
Streamlit| Web application interface
Pandas| Data processing
NumPy| Numerical operations
NetworkX| Knowledge graph operations
Plotly| Interactive visualizations
PyMuPDF| PDF processing
Python-docx| Word document processing
Scikit-learn| Machine learning
LangChain| AI application framework
LangChain OpenAI| AI model integration
FAISS| Vector similarity search
PyVis| Knowledge graph visualization
SQLite / Database module| User data management
Python-dotenv| Environment configuration

🏗️ System Architecture

The application follows a modular architecture.

             USER
               |
               v
       STREAMLIT INTERFACE
               |
               v
       USER AUTHENTICATION
               |
               v
       MAIN APPLICATION
               |
       +-------+--------+
       |       |        |
       v       v        v
    Resume   Job     Career
   Analyzer Explorer Assistant
       |       |        |
       +-------+--------+
               |
               v
        KNOWLEDGE GRAPH
               |
               v
         CAREER ROADMAP
               |
               v
       DATABASE & HISTORY

📂 Project Structure

CareerLens-AI/
│
├── app.py
├── requirements.txt
├── .env
│
├── database/
│   └── db.py
│
├── pages/
│   ├── dashboard.py
│   ├── resume_analyzer.py
│   ├── job_explorer.py
│   ├── knowledge_graph.py
│   ├── career_assistant.py
│   ├── roadmap_page.py
│   └── history.py
│
└── README.md

Note: This is the expected structure based on the imports in the main application. Adjust it to match the actual repository files.

⚙️ Installation & Setup

Step 1: Clone the Repository

git clone https://github.com/Sakshi-bidgar96/CareerLens-AI.git

Step 2: Open Project Folder

cd CareerLens-AI

Step 3: Create Virtual Environment

python -m venv .venv

Activate the environment on Windows:

.venv\Scripts\activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Configure Environment Variables

Create a ".env" file in the project root and add the API configuration required by your AI integration.

Never upload API keys or passwords to GitHub.

Step 6: Run the Application

streamlit run app.py

Open the local URL displayed in your terminal to access CareerLens AI.

📸 Application Screenshots

Add your actual application screenshots here.

![Login Page](screenshots/login.png)

![Dashboard](screenshots/dashboard.png)

![Resume Analyzer](screenshots/resume_analyzer.png)

![Knowledge Graph](screenshots/knowledge_graph.png)

![Career Roadmap](screenshots/career_roadmap.png)

🌟 Benefits

- Simplifies resume evaluation.
- Supports career exploration.
- Provides AI-assisted career guidance.
- Helps identify skill development opportunities.
- Combines multiple career-related tools in one platform.
- Provides a personalized user experience.

🔮 Future Scope

- Integration with live job portals.
- Advanced AI-based resume scoring.
- Automated resume improvement suggestions.
- LinkedIn profile analysis.
- Personalized learning recommendations.
- Interview preparation assistant.
- Advanced career prediction and recommendation system.

🎓 Project Objective

The main objective of CareerLens AI is to make career planning easier, smarter and more accessible by combining artificial intelligence, data processing and knowledge graph technologies.

👩‍💻 Team Members

This project is developed collaboratively by the following team members:

Sr. No.| Team Member Name
1| Sakshi Dhondiram Bidgar
2| Madhura Dattatreya Veer
3| Sanika Balaji Bavale

Project Title: AI Career Intelligence & Resume Analyzer

Project Name: CareerLens AI

GitHub: https://github.com/Sakshi-bidgar96

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>