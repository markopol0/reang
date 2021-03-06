"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
from corsheaders.defaults import default_headers
from decouple import config, Csv
import dj_database_url

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

PRIVATE_MEDIA_ROOT = config('PRIVATE_MEDIA_ROOT')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_extensions',
    'oauth2_provider',
    'social_django',
    # 'storages',
    'sslserver',
    # 'rest_framework.authtoken',
    'rest_framework_social_oauth2',
    # 'rest_framework_docs',
    'rest_framework',
    'corsheaders',
    'users.apps.UsersConfig',
]

AUTHENTICATION_BACKENDS = (
   # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # django-rest-framework-social-oauth2
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        # 'rest_framework.permissions.IsAdminUser'
    ],
    # 'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    # 'django_pdb.middleware.PdbMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_ROOT, 'templates')],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:3030',
    '127.0.0.1:3030'
)
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = default_headers + (
    # 'access-control-allow-credentials',
    # 'access-control-allow-methods',
    # 'access-control-allow-headers',
    # 'access-control-allow-origin',
    # 'x-forwarded-host',
    # 'session-id',
)

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

CSRF_COOKIE_NAME = "csrfmiddlewaretoken"
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE=True
# CSRF_USE_SESSIONS= True

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1')
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_PANELS = [
	    'debug_toolbar.panels.versions.VersionsPanel',
	    'debug_toolbar.panels.timer.TimerPanel',
	    'debug_toolbar.panels.settings.SettingsPanel',
	    'debug_toolbar.panels.headers.HeadersPanel',
	    'debug_toolbar.panels.request.RequestPanel',
	    'debug_toolbar.panels.sql.SQLPanel',
	    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
	    'debug_toolbar.panels.templates.TemplatesPanel',
	    'debug_toolbar.panels.cache.CachePanel',
	    'debug_toolbar.panels.signals.SignalsPanel',
	    'debug_toolbar.panels.logging.LoggingPanel',
	    'debug_toolbar.panels.redirects.RedirectsPanel',
	]
    SHOW_TOOLBAR_CALLBACK = True
else:
    RAISE_EXCEPTIONS= False
    SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['state']
SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'



AUTH_USER_MODEL = 'users.User'
SOCIAL_AUTH_USER_MODEL = 'users.User'
# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'

SOCIAL_AUTH_FACEBOOK_KEY = config('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from facebook. Email is not sent by default, to get it, you must request the email permission:
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email, age_range'
}

SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.11'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = 'https://127.0.0.1:3030/loggedin/facebook/'
SOCIAL_AUTH_LOGIN_ERROR_URL = 'https://127.0.0.1:3030/loggedin/error/'
# SOCIAL_AUTH_LOGIN_URL = 'https://dev.4ren4.com:8080/loggedin/facebook/'
# SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
# SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'  #Inactive users can be redirected to this URL when trying to authenticate.
# SOCIAL_AUTH_URL_NAMESPACE = 'users:social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
