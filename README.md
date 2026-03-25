# 🧠 Mindscape

**Mindscape** is a clean and beginner-friendly Django web project focused on **Artificial Intelligence (AI)** and **Machine Learning (ML)** learning content.  
It combines educational pages, user authentication, and project showcase sections into one simple, easy-to-navigate experience. ✨

Whether you are exploring AI/ML concepts for the first time or building with Django, Mindscape offers a practical structure for learning and extending web applications.

---

## 🌟 Why Mindscape?

- 📘 **Educational focus** on AI and ML topics
- 🔐 **Built-in authentication** (Sign up, Login, Logout)
- 🧩 **Modular Django app structure** for easy development
- 🗂️ **Project showcase pages** to present ideas and work
- 🚀 **Simple local setup** with SQLite for development

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend Framework | [Django](https://www.djangoproject.com/) (Python) |
| Frontend | HTML, CSS |
| Language | Python 3 |
| Database | SQLite (development) |

---

## 🗃️ Project Structure

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

## ✅ Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

---

## ⚙️ Installation & Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/TwinkleRathour/Mindscape.git
cd Mindscape
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

## 🧭 Available Pages

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

## 📄 License

This project is open source and available for educational purposes.
