from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# mongodb://admin:123.abc@@ds159400.mlab.com:59400/oildb

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'oildb',
        'HOST': 'ds159400.mlab.com',
        'PORT': 59400,
        'USER': 'admin',
        'PASSWORD': '123.Abc@',
        'AUTH_SOURCE': 'oildb',
    }
}
