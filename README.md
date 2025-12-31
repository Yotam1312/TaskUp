# 📚 TaskUp – Moodle Assignment Tracker

TaskUp is a student-focused system that helps track and manage Moodle assignments through a mobile-friendly API.

The system automatically fetches assignments from Moodle using web scraping and exposes a clean backend for future mobile apps.

---

## 🎯 What Does TaskUp Do?

- Secure login using Moodle credentials
- Automatically fetches all assignments from Moodle via web scraping
- Displays assignments with due dates and course information
- Distinguishes between pending, submitted, and archived assignments
- Designed to support mobile apps (Android & iOS)
- Built as a long-term, scalable student project

---

## 🏗️ High-Level Architecture
```
Mobile App (planned)
        ↓
  FastAPI Backend
        ↓
  Selenium Scraper
        ↓
      Moodle
```

> The backend currently combines API logic and scraping.  
> Database persistence, authentication tokens, and cloud deployment are part of the planned architecture.

---

## 🛠️ Tech Stack

| Component | Technology | Status |
|-----------|------------|--------|
| Backend API | Python, FastAPI | ✅ |
| Web Scraping | Selenium + Chrome | ✅ |
| Frontend | React + Capacitor | ✅ (separate repo) |
| Database | SQL Server (Azure) | 🔜 Planned |
| Authentication | JWT | 🔜 Planned |
| Security | Secure credential handling | 🔜 Planned |
| Cloud Hosting | Azure | 🔜 Planned |
| Containers | Docker | 🔜 Planned |
| Mobile Apps | Android & iOS | 🔜 Planned |
| Notifications | Firebase | 🔜 Planned |
| Testing | pytest | 🔜 Planned |

---

## 📁 Project Structure
```
TASKUPSERVER/
├── main.py               # FastAPI application entry point
├── moodle_scraper.py     # Selenium-based Moodle scraper
├── database.py           # Database layer (early POC / not persisted yet)
├── security.py           # Credential handling utilities (experimental)
├── models.py             # Pydantic request models
├── .env                  # Environment variables (not in git)
└── .gitignore            # Git ignore file


```

---

## 🚀 Installation & Running (Local)

### Prerequisites
- Python 3.10+
- Google Chrome installed

### Setup
```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

---

## ⚙️ Environment Notes

- The scraper requires Google Chrome to be installed.
- If needed, update the Chrome binary path in `moodle_scraper.py`.

---

## 🔌 API Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Verifies Moodle credentials and fetches basic user data |
| POST | `/pending_assignments` | Fetches assignments from Moodle via scraper |

> This represents the current Proof of Concept (POC) flow.  
> Future versions will persist data in a database and use JWT authentication.

---

## 🗺️ Roadmap

- [x] Moodle scraping with Selenium
- [x] FastAPI backend skeleton
- [x] JSON data contract
- [ ] SQL Server persistence (Azure)
- [ ] JWT authentication
- [ ] Assignment status management (pending / submitted / archived)
- [ ] Dockerization
- [ ] Cloud deployment (Azure)
- [ ] Android & iOS mobile apps
- [ ] Push notifications

---

## 👥 Team

This project is developed collaboratively by two Computer Science students as:
- A portfolio project
- A real-world system for students
- A foundation for a full mobile application

---

## 📄 License

MIT License

---

<p align="center">
  <b>TaskUp</b> – Never miss a deadline 🎓
</p>