# Task Management API

A Django-based RESTful API for user authentication and task management.

## Features
- **User Authentication**: Register and login using JWT tokens.
- **Task Management**: 
  - Create tasks.
  - View a list of tasks.
  - Delete tasks.

## Technologies Used
- Django
- Django REST Framework
- SimpleJWT for authentication

## Prerequisites
- Python 3.8+
- pip (Python package manager)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2.Create a virtual environment and activate it:
python -m venv env
source env/bin/activate       # On Mac/Linux
env\Scripts\activate          # On Windows


3.Install required dependencies:
pip install -r requirements.txt


4.Apply migrations to set up the database:
python manage.py migrate


5.Run the development server:
python manage.py runserver


API Endpoints
User Authentication
    Register: POST /auth/register/
    Login: POST /auth/login/
Task Management
    Create Task: POST /tasks/create/
    View Tasks: GET /tasks/
    Delete Task: DELETE /tasks/delete/<task_id>/
Testing the API
    Use Postman or cURL to test the API endpoints.
    Include JWT tokens in headers for authenticated requests.
    Required POSTMAN To Work with API(Post, Put, Send etc..) operations.
