# Photo Album Manager

A production-ready Django photo album management system with Cloudinary media storage, role-based access control, and Render deployment support.

## Features

- Django 6 application with Class-Based Views (List, Create, Update, Delete)
- Cloudinary integration for all image uploads and media storage
- PostgreSQL-ready database configuration via `DATABASE_URL`
- Role-based permission enforcement using Django auth and model permissions
- Render-friendly configuration with `DEBUG=False` by default
- Whitenoise static file support for production

## Setup

1. Create a virtual environment and install requirements:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with:

```env
SECRET_KEY=your_secret_key_here
DEBUG=False
USE_POSTGRES=True
USE_LOCAL_MEDIA=False
ALLOWED_HOSTS=yourdomain.com,localhost,127.0.0.1
DATABASE_URL=postgres://user:password@host:port/dbname
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

For local development, you can disable Postgres and use SQLite with local media storage:

```env
DEBUG=True
USE_POSTGRES=False
USE_LOCAL_MEDIA=True
```

3. Run migrations and create a superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Start the development server:

```bash
python manage.py runserver
```

## Render Deployment

- Add the project to Render as a Django web service.
- Set the environment variables in Render's dashboard using the same keys as above.
- Use `gunicorn recipe_project.wsgi` as the start command.
- Ensure a PostgreSQL database is provisioned and the `DATABASE_URL` secret points to it.

## Environment Variables

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `DATABASE_URL`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

## Notes

- Local media storage is disabled in production.
- Image uploads are handled via Cloudinary to ensure scalable and secure storage.
