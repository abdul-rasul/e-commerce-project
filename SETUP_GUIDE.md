# Django E-Commerce Project Setup Guide

This guide will help you set up and run the Django e-commerce project from scratch.

## Prerequisites

Before starting, make sure you have the following installed:

1. **Python 3.8+** - Check with: `python --version` or `python3 --version`
2. **pip** - Python package manager (usually comes with Python)
3. **Virtual Environment** (recommended) - `venv` or `virtualenv`

## Step-by-Step Setup

### 1. Create and Activate Virtual Environment

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Dependencies

Once your virtual environment is activated, install all required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Django 6.0
- asgiref
- sqlparse
- tzdata

### 3. Run Database Migrations

Django needs to set up the database tables. Run:

```bash
# Create migration files (if models exist)
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

This creates the SQLite database (`db.sqlite3`) with all necessary tables.

### 4. Create Superuser (Admin Account)

Create an admin account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter:
- Username
- Email (optional)
- Password (will be hidden)

### 5. Collect Static Files (Optional for Development)

For development, static files should work automatically. For production:

```bash
python manage.py collectstatic
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

You can also specify a port:
```bash
python manage.py runserver 8080
```

### 7. Access the Application

- **Homepage**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **About Page**: http://127.0.0.1:8000/about/
- **Contact Page**: http://127.0.0.1:8000/contact/
- **FAQ Page**: http://127.0.0.1:8000/faq/

## Project Structure

```
e-commerce-project/
├── config/           # Main project settings
├── core/            # Core app (homepage, about, contact, FAQ)
├── product/         # Product app (shop, products)
├── order/           # Order app (cart, checkout)
├── accaunt/         # Account app (login, registration, profile)
├── blog/            # Blog app
├── static/          # Static files (CSS, JS, images)
├── media/           # User-uploaded files (created automatically)
├── db.sqlite3       # Database file (created after migrations)
├── manage.py        # Django management script
└── requirements.txt # Python dependencies
```

## Common Commands

### Database Operations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (WARNING: deletes all data)
# Delete db.sqlite3, then run:
python manage.py migrate
```

### Django Shell
```bash
# Open Django shell
python manage.py shell
```

### Create New App
```bash
python manage.py startapp app_name
```

### Run Tests
```bash
python manage.py test
```

## Troubleshooting

### Issue: "No module named 'django'"
**Solution**: Make sure your virtual environment is activated and Django is installed:
```bash
pip install -r requirements.txt
```

### Issue: Static files not loading
**Solution**: 
1. Check `STATICFILES_DIRS` in `settings.py`
2. Make sure `django.contrib.staticfiles` is in `INSTALLED_APPS`
3. Run `python manage.py collectstatic` if needed

### Issue: "Table doesn't exist"
**Solution**: Run migrations:
```bash
python manage.py migrate
```

### Issue: "Port already in use"
**Solution**: Use a different port:
```bash
python manage.py runserver 8080
```

## Next Steps

1. **Add Product Models**: Define your product models in `product/models.py`
2. **Create Views**: Add views for shop, product details, etc.
3. **Set Up URLs**: Configure URL patterns for all apps
4. **Add Authentication**: Implement user registration and login
5. **Shopping Cart**: Implement cart functionality
6. **Payment Integration**: Add payment gateway (Stripe, PayPal, etc.)

## Development Tips

1. **Always use virtual environment** to avoid package conflicts
2. **Run migrations** after changing models
3. **Use Django admin** to manage data during development
4. **Check Django console** for error messages
5. **Use `DEBUG = True`** only in development (never in production!)

## Production Deployment Checklist

Before deploying to production:

- [ ] Set `DEBUG = False`
- [ ] Set `ALLOWED_HOSTS = ['yourdomain.com']`
- [ ] Generate new `SECRET_KEY` (keep it secret!)
- [ ] Set up proper database (PostgreSQL recommended)
- [ ] Configure static files serving
- [ ] Set up media files storage
- [ ] Use environment variables for sensitive data
- [ ] Enable HTTPS
- [ ] Set up proper logging
- [ ] Configure email backend
- [ ] Set up backup system

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)

---

**Happy Coding! 🚀**

