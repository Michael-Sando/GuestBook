GuestBook Django Application

Overview

The GuestBook Django Application is a simple web-based system that allows users to submit their names and messages through a form and view all submitted entries on a dedicated page.

This project demonstrates core Django concepts including models, forms, views, templates, and static file handling, along with a complete deployment workflow.

---

Features

* Homepage with user input form
* Save guest entries (name and message) to the database
* View all submitted entries on a list page
* Basic CSS styling for clean UI
* Automatic timestamp for each entry
* Deployment-ready configuration

---

Tech Stack

* Backend: Django (Python)
* Frontend: HTML, CSS (Django Templates)
* Database: SQLite (development)
* Deployment: Render
* Web Server: Gunicorn
* Static Files: WhiteNoise

---

📂 Project Structure


mysite/
│
├── manage.py
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── guestbook/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   │   └── guestbook/
│   │       ├── home.html
│   │       └── entry_list.html
│   └── static/
│       └── guestbook/
│           └── style.css

---


Key Learning Outcomes

This project helped reinforce:

* Django Models and database migrations
* Form handling using ModelForms
* Request/response lifecycle in Django
* Template rendering and static files
* Production configuration and deployment
* Git and GitHub workflow

---

Future Improvements

* Add user authentication
* Add edit/delete functionality
* Upgrade to PostgreSQL
* Add REST API (Django REST Framework)
* Integrate React frontend

---

Author
Michael Sando
Business Analyst | Aspiring Financial Solutions Architect
Focus: Accounting, Data Analytics & Software Development

---
This project is open-source and available for learning purposes.
