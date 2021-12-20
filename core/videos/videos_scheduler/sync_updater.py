from apscheduler.schedulers.background import BackgroundScheduler
#from core.videos.models import Videos
from videos.views import VideosViewSet
from pytz import utc
def start():
  scheduler = BackgroundScheduler(timezone=utc)
  Videos = VideosViewSet()
  scheduler.add_job(Videos.sync_vrank, "interval", minutes=5)
  scheduler.start()