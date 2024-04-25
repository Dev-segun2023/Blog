from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
<<<<<<< HEAD
<<<<<<< HEAD



    def ready(self):
        import account.signals
=======
>>>>>>> 0406121010b458144732d0919fddda79ac4f7055
=======


    def ready(self):
        import account.signals
>>>>>>> parent of 4bbdbee (deleted html not in template)
