from django.apps import AppConfig


class ProdFeedbackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prod_feedback'


    def ready(self):
        import prod_feedback.signals

