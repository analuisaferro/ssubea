
import os
from pathlib import Path
from . import envvars

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Read enviroment variables
env_vars = envvars.load_envvars(BASE_DIR)

db_name = env_vars['db_name']
db_user = env_vars['db_user']
db_host = env_vars['db_host']
db_passwd = env_vars['db_pw']
email_user = env_vars['email_sistema']
email_pass = env_vars['email_pw']

DEBUG = env_vars['debug_mode']
SECRET_KEY = env_vars['django_secret_key']


ALLOWED_HOSTS = ['*']

try:
    hCAPTCHA_PUBLIC_KEY = env_vars['hCAPTCHA_Public_Key']
    hCAPTCHA_PRIVATE_KEY = env_vars['hCAPTCHA_Secret_Key']
except:
    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY = ''

try:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env_vars['GOOGLE_OAUTH2_PUBLIC_KEY']
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env_vars['GOOGLE_OAUTH2_SECRET_KEY']

    SOCIAL_AUTH_FACEBOOK_KEY = env_vars['FACEBOOK_DEVELOPER_PUBLIC_KEY']
    SOCIAL_AUTH_FACEBOOK_SECRET = env_vars['FACEBOOK_DEVELOPER_SECRET_KEY']
except:
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''

    SOCIAL_AUTH_FACEBOOK_KEY = ''
    SOCIAL_AUTH_FACEBOOK_SECRET = ''


CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:3000', 'http://localhost:3000'
]

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:3000', 'http://localhost:3000']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third-party
    'bootstrap5',
    'fontawesomefree',
    #apps
    'core',
    'autenticacao',
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

ROOT_URLCONF = 'ssubea.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ssubea.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {   
    # 'default':{'ENGINE': 'django.db.backends.mysql'},
    # 'auth': {
    #     'ENGINE': 'django.db.backends.mysql',

    #     'NAME': 'usuarios_pmnf',
    #     'PORT': '',

    #     'USER': db_user,
    #     'PASSWORD': db_passwd,
    #     'HOST': db_host,
    # },
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'NAME': db_name,
        'PORT': '',

        'USER': db_user,
        'PASSWORD': db_passwd,
        'HOST': db_host,
    }
}
# DATABASE_ROUTERS = ['portal.dbrouter.DatabaseAppsRouter']
# DATABASE_APPS_MAPPING = {'auth': 'auth',
#                          'django': 'portal',
#                          'core': 'portal'}

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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

# Redirects

LOGIN_URL='/admin'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DEFAULT_FROM_EMAIL = 'Secretaria Municipal de Turismo e Marketing <turismo@sme.novafriburgo.rj.gov.br>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = email_user
EMAIL_HOST_PASSWORD = email_pass
X_FRAME_OPTIONS = 'SAMEORIGIN'
