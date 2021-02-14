from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from core.scraper import get_info
from core.models import Scraper


logger = get_task_logger(__name__)

@task(name='get_info_scraper')
def get_info_scraper():
    for x in Scraper.objects.all():
        sleep(x.scrape_frecuency)
        get_info(x.asset, x.url)
        print('Done')
