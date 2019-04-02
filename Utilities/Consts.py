import logging
import sys

LOGGING_FORMAT = "%(asctime)-4s %(levelname)-8s %(module)-22s:%(lineno)-4s %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, stream=sys.stdout)

COIN_SYMBOL = 'coin_symbol'
DATE_UTC = 'Date UTC'
CREATED_UTC = 'created_utc'

MAX_CHANGE_HEADER = 'open_max_change'
MAX_CHANGE_CLASSIFICATION = 'open_max_change_classification'
