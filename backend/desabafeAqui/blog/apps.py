from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals
