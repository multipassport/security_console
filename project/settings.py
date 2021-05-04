import os

from environs import Env

env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str('DB_ENGINE'),
        'HOST': env.str('DB_HOST'),
        'PORT': env.int('DB_PORT'),
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_LOGIN'),
        'PASSWORD': env.str('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

DEBUG = env.bool("DEBUG", default=False)

SECRET_KEY = env.str("SECRET_KEY")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
