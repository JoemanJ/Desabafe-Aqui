from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'perfis'

    def ready(self):
        import blog.signals
