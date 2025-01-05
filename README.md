
# To-Do List Application 📝

A fully functional To-Do List web application built using **Django**, providing features such as task creation, updates, deletion, user authentication, and task history management. This application allows users to securely manage their tasks and view a history of completed or deleted tasks.

---

## Features 🚀

- **User Authentication**: Secure login and registration functionality with Django's authentication system.
- **Task Management**:
  - Add new tasks with a simple, user-friendly interface.
  - Update existing tasks.
  - Delete tasks and move them to the history log.
- **Search Functionality**: Easily find tasks using the search bar.
- **Task History**: View and manage a list of previously deleted tasks.
- **Responsive Design**: Fully responsive UI for desktop and mobile devices.

---

# Project Structure 📂

todo-list-django/
├── ToDO/                    # Main project folder
├── app/                     # Main application folder
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── views.py             # Views (Business logic)
│   ├── models.py            # Database models
│   └── urls.py              # URL configurations
├── static/                  # Static files (CSS, Images)
├── templates/               # Project-level HTML templates
├── manage.py                # Django project management script
├── db.sqlite3               # SQLite database file

---

## Screenshots 📸

### 1. Home Page
![Screenshot 2025-01-05 100706](https://github.com/user-attachments/assets/6b96b257-6b5a-4210-ad62-f98f0c12cd5a)

![Screenshot 2024-12-17 123144](https://github.com/user-attachments/assets/71aba89e-ac8e-4757-9ad6-9492fc121ca3)

### 2. Add Task
![Screenshot 2024-12-17 092841](https://github.com/user-attachments/assets/f8c5118a-8e47-4504-be85-fb942acb8ddc)

### 3. Update Task
![Screenshot 2025-01-05 101020](https://github.com/user-attachments/assets/cd174e1c-77ef-440f-902b-b437cbc0f040)

### 4. Task History
![Screenshot 2024-12-17 123252](https://github.com/user-attachments/assets/8197af9b-0678-4e55-b92f-8538a8200c9b)

---

## Technologies Used 🛠️

- **Frontend**:
  - HTML5, CSS3
  - JavaScript
  - Bootstrap (Optional: Specify if used)
  
- **Backend**:
  - Django (Python)

- **Database**:
  - SQLite3 (default for Django)

- **Version Control**:
  - Git & GitHub

---

## Setup Instructions ⚙️

Follow these steps to set up the project locally:

### Prerequisites
- Python (>=3.8 recommended)
- Django (>=4.0)
- Git

### Steps

1. Clone the repository:
   
   git clone https://github.com/Akshatsingh14/To-Do-List.git
   cd todo-list-django

2. Set up a virtual environment:

   python -m venv venv
   venv\Scripts\activate  # Windows

3. Install dependencies.

4. Apply migrations to set up the database:

   python manage.py makemigrations
   python manage.py migrate

5. Run the development server:

   python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000

# How It Works ⚙️
  
  Authentication: 
    Users can register and log in.
    Each user has their own task list and history.

  Task Management:
    Users can add, edit, and delete tasks.
    Deleted tasks are moved to the "History" section for later reference.

  Search:
    Users can search for tasks by keywords.
  
  History:

    View and delete tasks from the history log.

#Contributing 🤝
Contributions are welcome! Feel free to submit a pull request or open an issue if you find a bug or have a suggestion.
