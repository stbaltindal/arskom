
import logging
logger = logging.getLogger(__name__)

import os
import sys
import uuid
import socket
import random

import requests

from time import sleep, time
from itertools import chain
from datetime import datetime
from contextlib import closing
from os.path import join, dirname

from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

from requests import ConnectionError

from readability import Document

from spyne.util.xml import get_xml_as_object
from spyne.util.six import BytesIO
from spyne.util.six.moves.urllib.parse import urlparse

from twisted.internet.task import LoopingCall
from twisted.internet.defer import DeferredList



from lxml import etree, html
from lxml.html import HTMLParser
from lxml.html.builder import E

class RssItem:
    def __init__(self, url, dt,title,summary):
        pass # TODO


def _scrape_url(item):
    url = item.link
    purl = urlparse(url)
    headers = {
        "User-Agent": "mlstore 1.0.0",
    }

    # fetch url
    if purl.scheme in ('http', 'https'):
        try:
            response = requests.get(url, headers=headers)
            data = response.text
            logger.info("Scraping %s", url)
        except socket.error as e:
            logger.exception(e)
            logger.error("Skipping %s", url)
            return

    else:
        logger.warning("Unknown url '%s'", url)
        return

    # fetch url
    document = Document(data, unwanted_tags=['img'])

    summary = document.summary(html_partial=True)
    summary = summary.replace(u"\u0091", "'") \
                     .replace(u"\u0092", "'") \
                     .replace(u"\u0093", '"') \
                     .replace(u"\u0094", '"')

    title = document.short_title()
    title = title.replace(u"\u0091", "'") \
                 .replace(u"\u0092", "'") \
                 .replace(u"\u0093", '"') \
                 .replace(u"\u0094", '"')

    sleep(2)  # prevent too fast scraping

    pub_date = item.pub_date
    if pub_date is None:
        logger.warning("%s has no publication date -- defaulting to now", url)
        pub_date = datetime.utcnow()

    return RssItem(
        url=url,
        dt=pub_date,
        title=title,
        summary=summary,
    )

