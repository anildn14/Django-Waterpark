"""
Django settings for waterpk project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("WP_SECRET_KEY", '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'water_park.apps.WaterParkConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'social_django'
]

REST_FRAMEWORK={
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
   
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'rest_framework.filters.DjangoFilterBackend',
    #     'rest_framework.filters.SearchFilter'),
}

AUTH_USER_MODEL='water_park.User' #change the built-in user model to ours custom model

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'waterpk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
'social_core.backends.open_id.OpenIdAuth',      # for Google authentication
'social_core.backends.google.GoogleOpenId',     # for Google authentication
'social_core.backends.google.GoogleOAuth2',     # for Google authentication
'social_core.backends.github.GithubOAuth2',     # for Github authentication
'social_core.backends.facebook.FacebookOAuth2', # for Facebook authentication
'social_core.backends.twitter.TwitterOAuth',    # for Twitter authentication
'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 

SOCIAL_AUTH_GITHUB_KEY = 
SOCIAL_AUTH_GITHUB_SECRET = 

SOCIAL_AUTH_FACEBOOK_KEY = 
SOCIAL_AUTH_FACEBOOK_SECRET = 

WSGI_APPLICATION = 'waterpk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'waterparkdb',
        'USER':
        'PASSWORD':
        'HOST':'localhost',
        'PORT':8000,
    }
}

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT=os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

LOGIN_URL='/waterparks/login_user'
LOGIN_REDIRECT_URL='/waterparks/login_user'

# BOTH COMMENTED AS WE WOULD NEED BOTH SUPERUSER LOGIN AND NORMAL LOGIN