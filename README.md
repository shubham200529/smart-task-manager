# Smart Task Management System

A modern Flask-based Task Management Web Application built using Python, PostgreSQL, REST APIs, WebSockets, Pandas, and NumPy.

---

# Project Description

Smart Task Management System is a full-stack web application that helps users efficiently manage their daily tasks. The project includes secure user authentication, task management APIs, PostgreSQL database integration, analytics processing using Pandas & NumPy, and real-time notifications using WebSockets.

The application allows users to:
- Register and login securely
- Add, complete, and delete tasks
- Track task progress
- View analytics dashboard
- Receive live task update notifications

This project was developed as part of a Python Development Internship Assignment.

---

# Features

## Authentication
- User Registration
- User Login
- Logout Functionality
- Password Hashing

---

## Task Management
- Add New Task
- View Tasks
- Complete Tasks
- Delete Tasks
- Task Priority Management

---

## Analytics Dashboard
Using Pandas & NumPy:
- Total Tasks
- Completed Tasks
- Pending Tasks
- Completion Percentage

---

## Real-Time Notifications
Using Flask-SocketIO:
- Live task update notifications
- Real-time dashboard refresh

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Development |
| Flask | Web Framework |
| PostgreSQL | Database |
| Flask-SQLAlchemy | ORM |
| Flask-Migrate | Database Migration |
| Flask-Login | Authentication |
| Flask-SocketIO | WebSockets |
| Pandas | Data Analytics |
| NumPy | Calculations |
| Bootstrap 5 | Frontend UI |
| HTML/CSS/JavaScript | Frontend Development |

---

# Project Structure

smart-task-manager/

├── app/

│   ├── routes/

│   ├── templates/

│   ├── static/

│   ├── analytics.py

│   ├── models.py

│   └── __init__.py

│

├── migrations/

├── .env

├── .gitignore

├── config.py

├── requirements.txt

├── run.py

└── README.md

---

# REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /register | Register User |
| POST | /login | Login User |
| GET | /tasks | Get All Tasks |
| POST | /tasks | Add Task |
| PUT | /tasks/<id> | Update Task |
| DELETE | /tasks/<id> | Delete Task |

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/shubham200529/smart-task-manager.git
