Django React Flashcards

A simple educational flashcards app built with Django REST Framework (backend) and React (frontend) to help users create, study, and manage decks of flashcards.

📌 Features

Create and manage Decks of flashcards

Add, edit, and delete Flashcards within decks

View all flashcards in a deck via a REST API

React frontend with simple Home and Dashboard pages

Fully functional CRUD API with Django REST Framework

Extensible structure for adding user accounts, study modes, and analytics

🛠 Tech Stack

Backend: Django, Django REST Framework

Frontend: React, React Router DOM

Database: SQLite (development), can be switched to PostgreSQL/MySQL for production

Other tools: Git, GitHub, VS Code

📁 Project Structure
flashcards_project/
├─ backend/            # Django backend
│  ├─ flashcards/      # Django app (models, serializers, views)
│  ├─ manage.py
│  └─ ...
├─ frontend/           # React frontend
│  ├─ src/
│  └─ ...
├─ .gitignore
└─ README.md

🚀 Getting Started
1. Clone the repo
git clone https://github.com/<your-username>/django-react-flashcards.git
cd django-react-flashcards

2. Setup Python environment
python3 -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
pip install -r backend/requirements.txt

3. Run Django backend
cd backend
python manage.py migrate
python manage.py runserver


API endpoints will be available at:

http://127.0.0.1:8000/api/decks/
http://127.0.0.1:8000/api/cards/

4. Run React frontend
cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000/

🔧 Usage

Access /dashboard in React to see the list of decks.

Use the API directly or connect React components to /api/decks/ and /api/cards/ for CRUD operations.

📚 Contributing

Fork the repo

Create a new branch (git checkout -b feature-name)

Make your changes

Commit your work (git commit -m "feat: your message")

Push (git push origin feature-name)

Open a Pull Request

📄 License

This project is licensed under the MIT License.
