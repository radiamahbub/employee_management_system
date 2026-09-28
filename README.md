# Employee Management System (EMS)

A web-based Employee Management System built with Django to manage employee information, authentication, attendance, leave records, and administrative operations through a centralized dashboard.

The project follows a modular Django architecture with separate applications for authentication, employees, attendance, leaves, and the main website.

---

## Overview

The Employee Management System (EMS) is designed to simplify employee administration by providing a centralized platform for managing employee records and related operations.

The application includes user authentication, employee CRUD operations, a dedicated management dashboard, and a responsive Bootstrap-based interface.

This project was developed as a practical full-stack Django application with a focus on clean architecture, reusable templates, database management, and maintainable code.

---

## Features

### Authentication

* User registration
* User login and logout
* Custom user model
* Password-based authentication
* Protected dashboard access
* Django authentication system
* CSRF protection

### Employee Management

* Add new employees
* View employee records
* View individual employee details
* Update employee information
* Delete employee records
* Employee listing
* Employee status management

### Attendance Management

* Employee attendance records
* Attendance tracking
* Daily attendance management
* Attendance overview

### Leave Management

* Employee leave records
* Leave tracking
* Leave status management
* Leave management workflow

### Dashboard

* Centralized management dashboard
* Employee statistics
* Attendance overview
* Leave overview
* Recent employee records
* Quick actions
* Sidebar navigation
* Account menu

### User Interface

* Responsive Bootstrap design
* Reusable Django templates
* Public website layout
* Authentication layout
* Dashboard layout
* Responsive forms and tables
* Clean and consistent interface

---

## Technology Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Backend programming       |
| Django           | Web framework             |
| SQLite           | Development database      |
| HTML5            | Page structure            |
| CSS3             | Styling                   |
| Bootstrap        | Responsive UI             |
| JavaScript       | Client-side functionality |
| Django Templates | Server-side rendering     |
| Git              | Version control           |
| GitHub           | Source code management    |

---

## Project Structure

```text
Employee_Management_System/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── employees/
│   ├── migrations/
│   ├── templates/
│   │   └── employees/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── attendance/
│   ├── migrations/
│   ├── templates/
│   │   └── attendance/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── leaves/
│   ├── migrations/
│   ├── templates/
│   │   └── leaves/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── main/
│   ├── templates/
│   │   └── main/
│   │       ├── home.html
│   │       ├── about.html
│   │       └── contact.html
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── auth_base.html
│   └── dashboard_base.html
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Application Architecture

The project is divided into multiple Django applications so that each part of the system has a clear responsibility.

### `main`

Handles public-facing pages such as:

* Home
* About
* Contact

### `accounts`

Handles authentication and user-related functionality.

### `employees`

Handles employee information and CRUD operations.

### `attendance`

Responsible for attendance-related functionality.

### `leaves`

Responsible for employee leave-related functionality.

### `config`

Contains the main Django project configuration, including:

* Settings
* Main URL configuration
* WSGI configuration
* ASGI configuration

This modular structure makes the project easier to maintain and expand.

---

## Template Architecture

The project uses three main base templates for different parts of the application.

```text
templates/
│
├── base.html
├── auth_base.html
└── dashboard_base.html
```

### `base.html`

Used for public-facing pages.

Includes:

* Navigation bar
* Public page layout
* Footer
* Bootstrap resources

Used by:

* Home
* About
* Contact

### `auth_base.html`

Used for authentication pages.

Includes a simple authentication-focused layout without the public website navigation.

Used by:

* Login
* Registration
* Future password reset pages

### `dashboard_base.html`

Used for authenticated dashboard pages.

Includes:

* Sidebar
* Dashboard navigation
* Top navigation bar
* Account section
* Main content area

Individual dashboard pages extend this template instead of duplicating the complete layout.

---

## Authentication Flow

The authentication system uses Django's authentication framework together with a custom user model.

The basic flow is:

```text
User
  │
  ├── Register
  │      │
  │      └── Account Created
  │
  └── Login
         │
         └── Authentication
                │
                └── Dashboard
                       │
                       └── Logout
```

The project uses a custom user model:

```python
class AuthUserModel(AbstractUser):
    pass
```

The custom model is configured in `settings.py`:

```python
AUTH_USER_MODEL = 'accounts.AuthUserModel'
```

Django sessions are used to maintain authenticated user sessions.

Future authentication improvements may include:

* Password reset
* Email verification
* Role-based permissions
* User profile management
* Remember-me functionality

---

## Database

SQLite is currently used as the development database.

Database configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

The database is managed through Django's migration system.

### Common Migration Commands

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Check migration status:

```bash
python manage.py showmigrations
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

For production, a more robust database such as PostgreSQL can be used.

---

## Installation

### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd Employee_Management_System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

The application will then be available through the local Django development server.

---

## Environment Variables

Sensitive configuration values should not be stored directly in the source code in a production environment.

Recommended environment variables include:

```text
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
```

A `.env` file can be used during development.

Example:

```text
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

The `.env` file should not be committed to Git.

It should be included in `.gitignore`.

---

## Security

The project follows Django's built-in security mechanisms where applicable.

Current security-related features include:

* CSRF protection
* Django password hashing
* Session-based authentication
* Django authentication framework
* Custom user model
* Template auto-escaping
* Password validation
* Django middleware security protections

For production deployment, additional configuration should be applied.

Recommended production settings include:

```python
DEBUG = False
```

A secure `SECRET_KEY` should be stored outside the source code.

Production configuration should also include:

* HTTPS
* Secure cookies
* Proper `ALLOWED_HOSTS`
* Secure CSRF configuration
* Secure session configuration
* Production database
* Proper static file handling
* Environment-based configuration

---

## Development Commands

### Start Development Server

```bash
python manage.py runserver
```

### Create Migrations

```bash
python manage.py makemigrations
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Open Django Shell

```bash
python manage.py shell
```

### Run Tests

```bash
python manage.py test
```

### Check Project Configuration

```bash
python manage.py check
```

### Collect Static Files

```bash
python manage.py collectstatic
```

---

## Testing

Testing is an important part of maintaining a reliable Django application.

The project can use Django's built-in testing framework for testing:

* Authentication
* Employee CRUD operations
* Model behavior
* Views
* URLs
* Forms
* Permissions
* Attendance functionality
* Leave functionality

Run the test suite with:

```bash
python manage.py test
```

As the project grows, automated tests can be added for each application.

A future goal is to increase test coverage for important business logic and user workflows.

---

## Git Workflow

Git is used for version control and project history.

A typical development workflow is:

```bash
git status
```

Create or switch to a feature branch:

```bash
git checkout -b feature/employee-management
```

After making changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add employee management CRUD"
```

Push the branch:

```bash
git push origin feature/employee-management
```

### Recommended Commit Style

Use clear and meaningful commit messages.

Examples:

```text
Add employee CRUD functionality
Fix authentication template path
Add dashboard base template
Update employee model
Improve dashboard navigation
Add registration functionality
Fix migration configuration
```

Small, focused commits make the project history easier to understand.

---

## Future Improvements

The project can be extended with additional features as development continues.

### Employee Management

* Employee profile pages
* Department management
* Designation management
* Employee search
* Employee filtering
* Employee profile photos
* Employee status management

### Attendance

* Daily attendance
* Check-in/check-out
* Attendance reports
* Monthly attendance summary
* Late attendance tracking

### Leave Management

* Leave request system
* Leave approval/rejection
* Leave balance
* Leave history
* Leave types

### Dashboard

* Employee statistics
* Attendance statistics
* Leave statistics
* Recent activities
* Charts and reports

### Authentication

* Password reset
* Email verification
* User profiles
* Role-based permissions
* Admin/user access control

### Technical Improvements

* PostgreSQL
* REST API
* Django REST Framework
* Automated testing
* Pagination
* Search and filtering
* Better error handling
* Production deployment
* CI/CD pipeline

---

## Production Deployment

The current project is intended for development and learning purposes.

Before deploying to production, the following areas should be configured properly.

### Application

* Set `DEBUG = False`
* Configure `ALLOWED_HOSTS`
* Use environment variables
* Configure production logging
* Configure static and media files

### Database

Move from SQLite to a production database such as PostgreSQL.

### Web Server

Use a production WSGI/ASGI server such as:

* Gunicorn
* Uvicorn

### Reverse Proxy

A reverse proxy such as Nginx can be used to handle:

* HTTPS
* Static files
* Request forwarding
* Domain configuration

### Security

Production deployment should include:

* HTTPS
* Secure cookies
* Strong secret key
* CSRF configuration
* Session security
* Proper host configuration
* Database security

### Deployment Platforms

The application can potentially be deployed using platforms such as:

* Railway
* Render
* PythonAnywhere
* VPS/cloud hosting

The exact deployment configuration depends on the hosting provider.

---

## Project Status

### Current

* Django project setup
* Multiple Django applications
* Custom user model
* Authentication structure
* User registration
* Login interface
* Public website pages
* Dashboard layout
* Employee CRUD functionality
* Bootstrap-based UI
* SQLite development database
* Migration setup

### In Development

* Attendance functionality
* Leave management functionality
* Dashboard statistics
* Role-based permissions
* Additional employee features
* Automated testing

### Planned

* PostgreSQL
* REST API
* Production deployment
* Advanced reports
* Email functionality
* Improved dashboard analytics

---

## Learning Goals

This project is being developed as a practical learning project to improve knowledge of:

* Python
* Django
* Django MVT architecture
* Django authentication
* Custom user models
* CRUD operations
* Database design
* Django ORM
* Migrations
* Templates
* Bootstrap
* URL routing
* Forms
* Git and GitHub
* Application architecture
* Authentication and authorization
* Testing
* Production deployment

The project is also intended to serve as a portfolio project demonstrating practical full-stack development skills.

---

## Author

**Radia Mahbub**

Full-Stack Developer

Interested in:

* Web Development
* Python
* Django
* Laravel
* React
* APIs
* AI-integrated applications
* Software Engineering

GitHub: `radiamahbub`

---

## License

This project is currently intended for educational and portfolio purposes.

A specific open-source license can be added when the project is ready for public distribution.
