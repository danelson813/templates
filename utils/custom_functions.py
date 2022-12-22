from loguru import logger

def greet():
    logger.info("called greet")
    print("Hey, there!")