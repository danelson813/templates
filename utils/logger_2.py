import sys
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, format="<red>[{level}]</red> Message : <green>{message}</green> @ {time}", colorize=True)

logger.success("Successfully changed format")