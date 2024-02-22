import environ
import os
from pathlib import Path



# BASE DIRECTORY

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = environ.Env(SECRET_KEY=(str))

DEBUG = environ.Env(DEBUG=(bool, False))

ALLOWED_HOSTS = ["localhost","127.0.0.1","djangostream","154.56.61.105","ias.nocciolli.com.br"]

CSRF_TRUSTED_ORIGINS = ["http://localhost","http://127.0.0.1","https://localhost","https://127.0.0.1","https://djangostream","https://154.56.61.105","https://ias.nocciolli.com.br"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # My apps
    # ------------------------------------------
    # Site
    'web.apps.WebConfig',
    #Authentication
    'authentication.apps.AuthenticationConfig',
    # Sistema
    'system.business.apps.BusinessConfig',
    'system.clients.apps.ClientsConfig',
    'system.dashboard.apps.DashboardConfig',
    'system.employees.apps.EmployeesConfig',  
    'system.notifications.apps.NotificationsConfig',  
    'system.products.apps.ProductsConfig',  
    'system.profiles.apps.ProfilesConfig',    
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {

    # DEVELOPMENT
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

}

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#              "CLIENT_CLASS": "redis.client.DefaultClient"
#          },
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'
USE_I18N = True

TIME_ZONE = 'America/Sao_Paulo'
USE_TZ = True

DATE_INPUT_FORMATS = ['%d/%m/%Y']
TIME_INPUT_FORMATS = ['%H:%M']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


# Login URLs

LOGIN_URL = '/auth/signin'


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.nocciolli.com.br'
EMAIL_HOST_USER = ('IAS', 'ias@nocciolli.com.br')
EMAIL_HOST_PASSWORD = 'muH32804'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'


# Default sessions settings

# SESSION_COOKIE_AGE = 86400
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# SESSION_SAVE_EVERY_REQUEST = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'