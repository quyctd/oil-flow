from .base import *

DEBUG = True

ALLOWED_HOSTS = ["54.169.183.183", 'oilflow.herokuapp.com']

#mongodb://admin:techkids69@ds263740.mlab.com:63740/oil-flow

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'oil-flow',
        'HOST': 'ds263740.mlab.com',
        'PORT': 63740,
        'USER': 'admin',
        'PASSWORD': 'techkids69',
        'AUTH_SOURCE': 'oil-flow',
    }
}

# CORS_REPLACE_HTTPS_REFERER = True
# HOST_SCHEME = "https://"
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 1000000
# SECURE_FRAME_DENY = True
