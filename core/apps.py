from django.apps import AppConfig
from core.task import get_info_scraper


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self) -> None:
        get_info_scraper()
