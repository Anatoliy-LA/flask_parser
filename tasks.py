import requests
from bs4 import BeautifulSoup
from celery import Celery
from collections import defaultdict
from conf import redis_address
import time


celery_app = Celery("celery", backend=redis_address, broker=redis_address)


@celery_app.task
def calc_tags(url):
    try:
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
    except Exception:
        return "Error! URL unreachable"

    result = defaultdict(int)
    for tag in soup.findAll():
        result[tag.name] += 1

    return result


@celery_app.task
def calc_tags_long(url):
    result = calc_tags(url)

    time.sleep(15)

    return result
