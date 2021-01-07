from django.apps import AppConfig

#REFERENCE FROM TEMPLATE ADDITION:
#For the template itself to be enabled. You must add it in the 'SETTINGS.PY' file
#For this you must take the 'BlogConfig' class and add it into the 'SETTINGS.PY'

class BlogConfig(AppConfig):
    name = 'blog'
