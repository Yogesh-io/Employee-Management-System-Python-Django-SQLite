# Employee Management System

A web-based Employee Management System developed using **Python, Django, SQLite, HTML, and CSS**. This project helps manage employee records through a simple web interface.

## Features

- User login and logout
- Add and register employee details
- View all employee records
- Update employee information
- Delete employee records
- Search employees by name or email
- Sort employees by name and salary
- Pagination for employee lists
- Upload employee profile pictures
- Upload employee resumes
- Form validation for employee information
- Store employee information in an SQLite database

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Django
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Authentication System
- **File Uploads:** Django File Handling

## Project Structure

```text
Employee_Management_System/
│
├── employee/
│   ├── migrations/
│   ├── templates/
│   │   └── employee/
│   │       ├── home.html
│   │       ├── add_employee.html
│   │       ├── view_employee.html
│   │       └── update_employee.html
│   ├── admin.py
│   ├── forms.py
│   ├── middleware.py
│   ├── models.py
│   ├── urls.py
│   ├── validators.py
│   └── views.py
│
├── employee_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   ├── employees_pic/
│   └── employees_resumes/
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project directory containing `manage.py`.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install django pillow
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the instructions to create your username and password.

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

Django administration panel:

http://127.0.0.1:8000/admin/

## Employee Information

The application supports the following employee information:

| Field | Description |
|---|---|
| Name | Employee's full name |
| Email | Employee's email address |
| Salary | Employee's salary |
| Date of Joining | Employee's joining date |
| Mobile | Employee's mobile number |
| Profile Picture | Employee's profile image |
| Resume | Employee's resume document |

## Application URLs

| URL | Function |
|---|---|
| `/` | Login page |
| `/add_emp/` | Add a new employee |
| `/view_emp/` | View employee records |
| `/update_emp/<id>/` | Update employee details |
| `/delete_emp/<id>/` | Delete an employee |
| `/logout/` | Logout |

## Learning Outcomes

Through this project, I learned:

- Django project and application structure
- Creating models and working with databases
- Building forms and validating user input
- Implementing CRUD operations
- Using Django authentication
- Handling file uploads
- Implementing search, sorting, and pagination
- Developing dynamic web pages using Django templates

## Future Enhancements

- Add employee departments and job titles
- Create an employee dashboard with statistics
- Implement role-based access control
- Add automated tests
- Deploy the application online

## Author

**Your Name**

- GitHub: (https://github.com/Yogesh-io)
- LinkedIn: (https://www.linkedin.com/in/yogesh-shete01/)

## License

This project was developed for educational and portfolio purposes.
