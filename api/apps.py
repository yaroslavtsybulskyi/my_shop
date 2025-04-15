from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the api app
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
