from django.apps import AppConfig


class BillingsoftwareAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BillingSoftware_App'


    def ready(self):
        import BillingSoftware_App.signals