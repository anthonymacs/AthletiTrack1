
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'django-insecure-ndL3MVQPk6xXJCM5wMnE5HChnq_KKn_Dj1uGisXzZJGD1sePzpYEaSiX6kPAg4vQ4AI'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    '.ngrok-free.app',
    '.trycloudflare.com',
    '.onrender.com',
]


CSRF_TRUSTED_ORIGINS = [
    "https://*.ngrok-free.app",  # allow any ngrok subdomain
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_q',

    # Local apps
    'users',
    'athletes',
    'coaches',
    'events',
    'reports',
    'core',

    'audits',

    'pwa',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'athletitrack.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.nav_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'athletitrack.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'athletitrack_db',
        'USER': 'root',      # Laragon's default username
        'PASSWORD': 'admin123456',      # Laragon's default password is empty
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MAILTRAP_API_TOKEN = "9dfaaab3ee38d4e9eb0c1a3467c05445"
MAILTRAP_INBOX_ID = "4134638" 


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# athletitrack/settings.py
AUTH_USER_MODEL = 'users.CustomUser'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = '/' # Optional: where to go after logout


Q_CLUSTER = {
    'name': 'athletitrack_cluster',
    'workers': 4,
    'recycle': 500,
    'timeout': 60,
    'compress': True,
    'save_limit': 250,
    'queue_limit': 500,
    'cpu_affinity': 1,
    'label': 'Django Q',
    'orm': 'default', # Use the default Django database
    'django_timezone': True,
}

SESSION_COOKIE_AGE = 60 * 60 * 2  # 2 hours
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'AthletiTrack <johnpatrick.camposano@evsu.edu.ph>'

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '0cfdbdcc956818'
EMAIL_HOST_PASSWORD = 'ae7005c85f8b29'
EMAIL_PORT = '2525'



PWA_APP_NAME = 'AthletiTrack'
PWA_APP_DESCRIPTION = "Yearly Performance Monitoring & Event Management for Athletes"
#PWA_APP_THEME_COLOR = '#0d6efd'
PWA_APP_THEME_COLOR = "#ffffff"
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'portrait'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/icons/icon-192x192.png',
        'sizes': '192x192'
    },
    {
        'src': '/static/icons/icon-512x512.png',
        'sizes': '512x512'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        "src": "/static/icons/icon-192x192.png",
        "sizes": "192x192"
    },
    {
        "src": "/static/icons/icon-512x512.png",
        "sizes": "512x512"
    }
]
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'static/js', 'serviceworker.js')

