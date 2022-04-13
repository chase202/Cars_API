# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lgl(2@y*(%s*rorqkx1#x1%xqtfzeoph=dkpj1nek4&2kvj702'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database', 
        'HOST': 'localhost', 
        'USER': 'root',
        'PASSWORD': 'Password2022'
    }
}