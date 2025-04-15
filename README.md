🛒 My Shop — Django Oscar E-commerce Project

My Shop is a production-ready e-commerce platform built with Django Oscar.

It includes:
• ✅ REST API with Django REST Framework
• 🔐 JWT authentication
• 📄 Swagger UI documentation
• 💰 PayPal sandbox integration
• 📦 Product catalogue, basket, checkout, and order management
• 🧪 Django Silk for profiling (optional)
• 🚀 Deployment on PythonAnywhere

⸻

🔧 Getting Started (Locally)

1. Clone the repository

```
git clone https://github.com/yourusername/my_shop.git
cd my_shop
```

2. Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a .env file and add your secrets

```
SECRET_KEY=your-secret-key
PAYPAL_API_USERNAME=your-paypal-sandbox-username
PAYPAL_API_PASSWORD=your-paypal-sandbox-password
PAYPAL_API_SIGNATURE=your-paypal-sandbox-signature
```

5. Apply migrations

```
python manage.py migrate
```

6. Create a superuser

```
python manage.py createsuperuser
```

7. Run the development server

```
python manage.py runserver
```

⸻

🔐 Authentication (JWT)

API uses JWT tokens. To authenticate:
• POST /api/token/ — get access and refresh tokens
• POST /api/token/refresh/ — refresh your access token

Use the “Authorize” button in Swagger UI to input your JWT as:
Bearer

⸻

📘 API Docs

Swagger documentation is available at:
/swagger/

⸻

🎛 Admin and Dashboard
• Django Admin: /admin/
• Oscar Dashboard: /dashboard/ (staff only)

⸻

💳 PayPal Integration

PayPal Express Checkout is integrated using sandbox mode.
Create sandbox credentials at https://developer.paypal.com

Set your credentials in the .env file.

⸻

🚀 Deployment on PythonAnywhere
1. Upload your code to PythonAnywhere
2. Create and activate virtualenv
3. Install dependencies: pip install -r requirements.txt
4. Set environment variables using .env
5. In the Web tab:
• Set the WSGI file to point to your Django app
• Set /static/ → /home/yourusername/my_shop/static/
• Set /media/ → /home/yourusername/my_shop/media/
6. Run:
• python manage.py collectstatic
• python manage.py migrate
7. Reload the web app

Make sure you set:
DEBUG = False
ALLOWED_HOSTS = [‘yourusername.pythonanywhere.com’]

⸻

⚡ Performance (Optional)

To enable Silk profiling:
• Add 'silk' to INSTALLED_APPS (only if DEBUG is True)
• Add 'silk.middleware.SilkyMiddleware' to MIDDLEWARE
• Visit /silk/ to see profiling data

⸻

🛡 Security

The app includes:
• CSRF, XSS, and SQL injection protection via Django
• Secure cookies and HTTPS redirects when DEBUG = False
• LocMemCache enabled by default (can be replaced with Redis or Memcached)

⸻

🧪 Technologies Used
• Django 5.2
• Django Oscar
• PostgreSQL or SQLite (default)
• Django REST Framework
• drf-yasg (Swagger)
• SimpleJWT
• PayPal SDK
• Silk (dev-only)
