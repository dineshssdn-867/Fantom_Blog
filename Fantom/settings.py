"""
Django settings for Fantom project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku
import cloudinary
import cloudinary_storage

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hd$3k3%9m#7^4j!ng@!sudq-kx0l$#yp1g!81p*hz97dl02^=q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['https://d-fantom-blog.herokuapp.com/', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
    'users',
    'crispy_forms',
    'captcha',
    'pwa',
    'contact',
    'myarchive',
    'cloudinary',
    'cloudinary_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
]

ROOT_URLCONF = 'Fantom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Fantom.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/myview'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

RECAPTCHA_PUBLIC_KEY = '6LdbxPsUAAAAAJhoNMgMT8UjrQJv4FPcDuMW8f53'
RECAPTCHA_PRIVATE_KEY = '6LdbxPsUAAAAAOH80fY1ZDsqDNZ6n3YPJXZwBzHW'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'  # storing session using serializer
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # This is for storing sessions in cache

PWA_APP_NAME = "D's Blog"
PWA_APP_DESCRIPTION = "A blog is a discussion or informational website published on the World Wide Web consisting of discrete, often informal diary-style text entries. Posts are typically displayed in reverse chronological order, so that the most recent post appears first, at the top of the web page"
PWA_APP_BACKGROUND_COLOR = '#000000'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_THEME_COLOR = '#0A0302'
PWA_APP_ICONS = [
    {
        'src': 'static/img/ds-d-s-purple-letter-logo-design-with-creative-liquid-effect-flowing-vector-illustration-MFR65B.png',
        'sizes': '160x160', 'purpose': 'any maskable',
        'src': 'static/img/ds-d-s-purple-letter-logo-design-with-creative-liquid-effect-flowing-vector-illustration-MFR65B.png',
        'sizes': '512x512', 'purpose': 'any maskable'}
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/img/ds-d-s-purple-letter-logo-design-with-creative-liquid-effect-flowing-vector-illustration-MFR65B.png',
        'sizes': '160x160'}
]
PWA_APP_SPLASH_SCREEN = [{'src': '/static/images/571658cd2ec465a08e2dc2cf30258023.png',
                          'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'}]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
PWA_APP_DEBUG_MODE = True

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dineshscloud',
    'API_KEY': '858455229732434',
    'API_SECRET': 'VTDlyF-OhpkS9hOvqxxBCMqGT3A',
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



django_heroku.settings(locals())
