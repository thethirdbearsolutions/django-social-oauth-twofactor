from django.apps import AppConfig

class Config(AppConfig):
    name = 'django_social_oauth_two_factor'

    def ready(self):
        pass
