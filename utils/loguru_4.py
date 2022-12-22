from loguru import logger

logger.remove(0)

logger.add("out.log")
logger.success("Written message to log file")