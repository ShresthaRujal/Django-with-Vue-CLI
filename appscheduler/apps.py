from django.apps import AppConfig

class AppschedulerConfig(AppConfig):
    name = 'appscheduler'

    def ready(self):
        from appscheduler import scheduler
        scheduler.start()