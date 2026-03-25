# Final Mindscape

**Final Mindscape** is a web application built with Django that serves as a platform exploring topics in Artificial Intelligence and Machine Learning. It provides informational pages about AI and ML concepts, user authentication (sign up / log in / log out), and a project showcase.

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend Framework | [Django](https://www.djangoproject.com/) (Python) |
| Frontend | HTML, CSS |
| Language | Python 3 |
| Database | SQLite (development) |

---

## Project Structure

```
finalmindscape/
├── config/                  # Django project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Root URL configuration
│   ├── wsgi.py              # WSGI entry point
│   └── asgi.py              # ASGI entry point
├── mainapp/                 # Main Django application
│   ├── migrations/          # Database migrations
│   ├── static/              # App-level static files (CSS)
│   ├── templates/           # HTML templates
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   └── views.py
├── manage.py                # Django management script
└── README.md
```

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

---

## Installation & Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/TwinkleRathour/finalmindscape.git
cd finalmindscape
```

### 2. Create and activate a virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux / macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. (Optional) Create a superuser for the Django admin panel

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The application will be available at **http://127.0.0.1:8000/**.

---

## Available Pages

| URL | Description |
|-----|-------------|
| `/` | Home / Landing page |
| `/login/` | Login page |
| `/signup/` | Sign-up page |
| `/logout/` | Logout |
| `/ml/` | Machine Learning page |
| `/ai/` | Artificial Intelligence page |
| `/aboutus/` | About Us page |
| `/project/` | Projects page |
| `/admin/` | Django admin panel |

---

## License

This project is open source and available for educational purposes.
