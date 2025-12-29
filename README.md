# 📚 TaskUp - Moodle Assignment Tracker

A mobile app for students to track and manage Moodle assignments.

---

## 🎯 What Does It Do?

- Login with your Moodle credentials
- Automatically fetch all assignments via web scraping
- Track submitted vs. pending assignments
- Push notifications for deadline reminders

---

## 🛠️ Tech Stack

| Component | Technology | Status |
|-----------|------------|--------|
| Backend | Python, FastAPI | ✅ |
| Frontend | React + Capacitor | ✅ (separate repo) |
| Scraping | Selenium + Chrome | ✅ |
| Database | SQL Server | 🔜 Planned |
| Security | Fernet Encryption | 🔜 Planned |
| Notifications | Firebase | 🔜 Planned |

---

## 📁 Project Structure

```
TASKUPSERVER/
├── src/                  # Helper modules
├── main.py               # FastAPI server entry point
├── models.py             # Database models
├── moodle_scraper.py     # Moodle web scraping script
└── homepage.html         # Homepage for testing
```

---

## 🚀 Installation & Running

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

## ⚙️ Environment Setup

Make sure Chrome is installed at:
```
C:\Program Files\Google\Chrome\Application\chrome.exe
```

Or update the path in `moodle_scraper.py`.

---

## 📱 App Flow

```
POST /login                     POST /pending_assignments
     │                                    │
     ▼                                    ▼
Scrape Moodle                    Scrape Moodle
(to verify credentials)          (fetch assignments)
     │                                    │
     ▼                                    ▼
Return:                          Return:
- success: true/false            - name
- name                           - assignments[]
- message                        - login_ok
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Verify Moodle credentials (runs scraper to validate) |
| POST | `/pending_assignments` | Fetch assignments from Moodle via scraper |

---

## 📝 Assignment JSON Structure (from scraper)

```json
{
  "title": "תיבת הגשה למשלה 2",
  "course": "ניהול מסדי נתונים",
  "due_date": "31/12/2025",
  "due_time": "23:55",
  "link": "https://moodle.ruppin.ac.il/mod/assign/view.php?id=56233",
  "name": "יוסי"
}
```

---

## 🔒 Security (Planned)

- [ ] Encrypt stored passwords with **Fernet**
- [ ] Add JWT token authentication
- [ ] Store assignments in DB instead of scraping each time

---

## 📄 License

MIT License

---

<p align="center">
  <b>TaskUp</b> - Never miss a deadline! 🎓
</p>
