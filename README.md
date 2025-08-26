# 🗳️ Poll System with Results Visualization

This is a full-stack poll management web application built as part of a machine test assessment. It allows user registration, poll creation by admins, voting by users, and visual display of poll results using charts.

---

## 📌 Features

### ✅ Core Functionality

- **User Authentication**
  - Registration and login system
  - Only logged-in users can vote
  - One vote per user per poll

- **Poll Management (Admin)**
  - Admin can create polls with a question and multiple options
  - Polls stored in a persistent database

- **Voting System**
  - Users can view and vote on active polls
  - One vote per poll per user enforced

- **Results Page**
  - Shows total votes and percentage share per option
  - Chart-based visualization (e.g., pie/bar using Chart.js)

---

### 🌟 Bonus Features (Implemented)

- [ ] Multiple active polls
- [ ] Poll expiry dates
- [ ] "My Votes" section
- [ ] Export results as CSV


---

## 🛠️ Tech Stack

- **Backend:** `Django` 
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 
- **Database:** SQLite 
- **Charting:** Chart.js for data visualization

---

## 🚀 Getting Started

### 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

Create Virtual Environment (Python)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install Dependencies

pip install -r requirements.txt


Run Migrations

python manage.py migrate


Start the Development Server

python manage.py runserver
Open http://127.0.0.1:8000 in your browser.

🔐 Admin Access
Username: indran
Password: 123