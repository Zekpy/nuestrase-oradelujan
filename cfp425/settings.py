"""
Django settings for cfp425 project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*0=4vrz(uk+az*mvialswfookkgtnu9prer#_#@*@2iv79k%w$'

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
    
    'allauth', #APP de auth0all
    'allauth.account',#APP de auth0all
    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',#APP de auth0all
    'inicio',#APP de inicio
    "crispy_forms", #Formularios
    "crispy_bootstrap5", #formularios
    'allauth.socialaccount.providers.google',

]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}
LOGIN_URL = '/accounts/login/'  # Ruta de inicio de sesión manejada por Allauth
SOCIALACCOUNT_LOGIN_ON_GET = True  # Opcional, para que la opción de Google se muestre sin necesidad de hacer clic en un botón.

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5" #Uso de templates de crispy forms

CRISPY_TEMPLATE_PACK = "bootstrap5" #Uso de templates de crispy forms
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",#Uso de auth0all
]
SITE_ID=1
ROOT_URLCONF = 'cfp425.urls'



LOGIN_REDIRECT_URL = 'index'

AUTHENTICATION_BACKENDS = [


    #Agregamos esto para que la autenticacion se hgaa desde el backend
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),  # carpeta templates en raiz del proyecto para una mejor organizacion
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',
                 
            ],
        },
    },
]

WSGI_APPLICATION = 'cfp425.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-ar' #Idioma predeterminado Español/Argentina

TIME_ZONE = 'America/Buenos_Aires' #Zona horaria de Argentina

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Ruta a la carpeta "static" en la raíz del proyecto
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


############## CONFIGURACIONES ADICIONES PARA USAR EMAIL #######################

if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #Envia un  mensaje por consola para autenticar a un usuario
else:
    #EMAIL_BACKEND: miconfiguraciondecorreo 
    # 
    pass