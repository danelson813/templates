import sys
from loguru import logger

logger.remove(0)

logger.add(sys.stderr, format="{time:HH:mm:SS} | {level} | {extra[ip]} | {message}")
context_logger = logger.bind(ip="192.168.0.1")

context_logger.info('Pinging IP')
