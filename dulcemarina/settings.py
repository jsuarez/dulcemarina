"""
Django settings for dulcemarina project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

#CKEDITOR_UPLOAD_PATH = [os.path.join(BASE_DIR, 'static/uploads')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u&)ia!hpvb_l5-n0l4nh42ip3d)9g@m7wh(b1ugv@60lb*#i&7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['http://dulcemarina.pythonanywhere.com/','www.dulcemarina.com.ar','dulcemarina.com.ar','http://www.dulcemarina.com.ar','http://dulcemarina.com.ar']
#

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'productos',
    'imagekit',
    'contact_form',
    'ckeditor',
    'deployer',
    'debug_toolbar',
    'ajustes',
    'servicios',
    'nosotros',
    'sliderfotos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dulcemarina.urls'

WSGI_APPLICATION = 'dulcemarina.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dulcemarina',
        'USER': 'root',
        'PASSWORD': '92807320',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Mendoza'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
INTERNAL_IPS = ("127.0.0.1",)
MEDIA_URL = '/media/'

#STATIC_ROOT = '/Users/juan/Sites/dulcemarina/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


EMAIL_HOST = 'localhost'

EMAIL_PORT = 25

EMAIL_HOST_USER = 'info@dulcemarina.com.ar'

EMAIL_HOST_PASSWORD = '1234'

#Para la implementacion de ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Styles', 'Format',
             '-', 'TextColor', 'BGColor',
             '-', 'SpellChecker', 'Scayt',
             '-', 'Maximize',
             ],
            ['HorizontalRule',
             '-', 'Image', 'Iframe', 'Flash', 'Table', 
             '-', 'BulletedList', 'NumberedList',
             '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord',
             '-', 'SpecialChar',
             '-', 'Source',
             ]
        ],
        'language': 'es',
        'scayt_sLang': 'es_ES',
        'wsc_lang': 'es_ES',
        'extraAllowedContent': 'iframe[src,width,height,frameborder,style]',
        'width': '100%',
    },
}

try:
    from settings_local import *
except ImportError:
    pass
