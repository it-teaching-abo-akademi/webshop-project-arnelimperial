import django_heroku

import os

from pathlib import Path

from decouple import config, Csv

from django.conf import settings

from corsheaders.defaults import default_headers

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# Application definition
# ------------------------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    "django.contrib.sites",
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.forms',
]
THIRD_PARTY_APPS = [
    'crispy_forms',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'webpack_loader',
    'whitenoise.runserver_nostatic',
    'corsheaders',
    # 'markdown_deux',
]

LOCAL_APPS = [
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',
    'merchandises.apps.MerchandisesConfig',
    'carts.apps.CartsConfig',
    'purchases.apps.PurchasesConfig',
   
    'initial.apps.InitialConfig',


]


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  
]

# General
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'webshop.urls'

WSGI_APPLICATION = 'webshop.wsgi.application'

TIME_ZONE = "Europe/Helsinki"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True

FORM_RENDERER = "django.forms.renderers.TemplatesSetting"


# Authentication
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

AUTH_USER_MODEL = 'users.User'

#LOGIN_REDIRECT_URL = "/"
# LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_REDIRECT_URL = 'client-app'

# LOGIN_URL = 'account_login'

# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = True

ACCOUNT_AUTHENTICATION_METHOD = "email"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_ADAPTER = "users.adapters.AccountAdapter"

# SOCIALACCOUNT_ADAPTER = "users.adapters.SocialAccountAdapter"

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_LOGOUT_REDIRECT_URL = "/"

#ACCOUNT_FORMS = {'signup': 'users.forms.RegistrationForm'}


# Templates
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'build'),
            os.path.join(BASE_DIR, 'templates'),
            ],
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





# Security
# ------------------------------------------------------------------------------

SESSION_COOKIE_HTTPONLY = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

if not settings.DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)

    SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)

    CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)

    SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=18408206, cast=int) #60

    SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)

    SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)

    SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', default=True, cast=bool)

    SECURE_REFERRER_POLICY = config('REFERRER_POLICY', default='same-origin')

    CORS_REPLACE_HTTPS_REFERER = True
    

# Password Hashers
# ------------------------------------------------------------------------------
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",

]


# Password Validation
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 5,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# EMAIL
# ------------------------------------------------------------------------------

EMAIL_FILE_PATH =  os.path.join(BASE_DIR, 'tmp/notifications')
EMAIL_BACKEND = config(
    'EMAIL_BACKEND', default='django.core.mail.backends.filebased.EmailBackend'
)

EMAIL_TIMEOUT = 5

DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

SERVER_EMAIL = config('SERVER_EMAIL', default=DEFAULT_FROM_EMAIL)

EMAIL_SUBJECT_PREFIX = config('EMAIL_SUBJECT_PREFIX', default="Nurtsrx WebShop")


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = config('ADMIN_URL', default='admin/')

ADMINS = [("""Arnel Imperial""", config('ADMIN_EMAIL'))]

MANAGERS = ADMINS



# django-rest-framework
# -------------------------------------------------------------------------------

# DEFAULT_RENDERER_CLASSES = (
#     'rest_framework.renderers.JSONRenderer',
# )

# if DEBUG:
#     DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + ('rest_framework.renderers.BrowsableAPIRenderer',)
    
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        #"rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        #"rest_framework.permissions.IsAuthenticated",
    ],
    #"DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',

    'PAGE_SIZE': 10
}

# django-rest-auth
# -------------------------------------------------------------------------------


# Django-cors-header
# ------------------------------------------------------------------------------

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'https://nurtsrx.herokuapp.com',
    'http://localhost',
]
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://nurtsrx.herokuapp.com'
)

CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)

CORS_ALLOW_HEADERS = default_headers + (
    'Access-Control-Allow-Origin',
)

CORS_PREFLIGHT_MAX_AGE = 86400

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000', 
    'nurtsrx.herokuapp.com',
]

# CORS_ALLOW_HEADERS = [
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# ]
# Webpack-loader
# ------------------------------------------------------------------------------

# WEBPACK_LOADER = {
#     'DEFAULT': {
#             'BUNDLE_DIR_NAME': 'bundles/',
#             'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json'),
#         }
# }

# WEBPACK_LOADER = {
#     "DEFAULT": {
#         "CACHE": not DEBUG,
#         "BUNDLE_DIR_NAME": "frontend/build/static/",
#         "STATS_FILE": os.path.join(BASE_DIR, "frontend", "build", "bundle-stats.json"),
#     }
# }

# Database
# ------------------------------------------------------------------------------

if settings.DEBUG: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'AUTH_SOURCE': config('DB_NAME'),
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }

# Django-heroku
# ------------------------------------------------------------------------------

django_heroku.settings(locals())


# STATIC
# ------------------------------------------------------------------------------

CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, 'build', 'static')
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATIC_ROOT = os.path.join(BASE_DIR, 'build', 'assets')
FAVICON = os.path.join(BASE_DIR, 'build', 'assets')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build', 'static'),
    os.path.join(BASE_DIR, 'public', 'assets')
]

# WHITENOISE_INDEX_FILE = True

# WHITENOISE_ROOT = os.path.join(BASE_DIR, 'frontend', 'build')

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# # MEDIA
# # ------------------------------------------------------------------------------


MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, 'build', 'media')











# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



