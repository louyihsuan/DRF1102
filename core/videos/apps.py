from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'
    
    def ready(self):
        print("Starting Scheduler ...")
        from .videos_scheduler import sync_updater
        sync_updater.start()