from apscheduler.schedulers.background import BackgroundScheduler
#from core.videos.models import Videos
from videos.views import VideosViewSet

def start():
  scheduler = BackgroundScheduler()
  Videos = VideosViewSet()
  scheduler.add_job(Videos.sync_vrank, "interval", minutes=1)
  scheduler.start()