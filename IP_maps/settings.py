"""
Django settings for IP_maps project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from django.urls import reverse_lazy
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=r@^1g#70=#8dea*#i7op2)b-zodvla4xe40n7zmkk*mn%3^!)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',
    'ckeditor',
    'ckeditor_uploader',
    'colorful',
    'adminsortable',
    'djeym',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'IP_maps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IP_maps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = reverse_lazy('home')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# django-ckeditor
# https://github.com/django-ckeditor/django-ckeditor
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_FILENAME_GENERATOR = 'djeym.utils.get_filename'
CKEDITOR_THUMBNAIL_SIZE = (300, 300)
CKEDITOR_FORCE_JPEG_COMPRESSION = True
CKEDITOR_IMAGE_QUALITY = 40
CKEDITOR_IMAGE_BACKEND = 'pillow'
CKEDITOR_ALLOW_NONIMAGE_FILES = False  # False - Only image files. (At your discretion)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    },
    'djeym': {
        'toolbar': 'full',
        'height': 400,
        'width': 362,
        'colorButton_colors': 'F44336,C62828,E91E63,AD1457,9C27B0,6A1B9A,'
                              '673AB7,4527A0,3F51B5,283593,2196F3,1565C0,'
                              '03A9F4,0277BD,00BCD4,00838F,009688,00695C,'
                              '4CAF50,2E7D32,8BC34A,558B2F,CDDC39,9E9D24,'
                              'FFEB3B,F9A825,FFC107,FF8F00,FF9800,EF6C00,'
                              'FF5722,D84315,795548,4E342E,607D8B,37474F,'
                              '9E9E9E,424242,000000,FFFFFF',
        'colorButton_enableAutomatic': False,
        'colorButton_enableMore': True
    }
}

# (If a non-authenticated user requests an editor page.)
# (Если не аутентифицированный пользователь запросит страницу редактора.)
LOGIN_URL = '/admin/'  # or change to your URL

# Required for django-admin-sortable
# https://github.com/alsoicode/django-admin-sortable#configuration
CSRF_COOKIE_HTTPONLY = False

# The API key is used in the free and paid versions.
# You can get the key in the developer’s office - https://passport.yandex.com/
# ( API-ключ используется в свободной и платной версиях.
#   Получить ключ можно в кабинете разработчика - https://developer.tech.yandex.ru/ )
DJEYM_YMAPS_API_KEY = 'ce0e27f9-fae4-4c1a-8c1b-217f3554e276'

# For paid use API --> True
# ( Для платного использования --> True )
DJEYM_YMAPS_API_KEY_FOR_ENTERPRISE = False

# Map download mode. Default = 'release'
# (Режим загрузки карт.)
# DJEYM_YMAPS_DOWNLOAD_MODE = 'debug'