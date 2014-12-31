#-*- coding: UTF-8 -*-

import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger("simple")

#"applecation" code

logger.debug("debug message")
logger.info("info message")
logger.critical("critical message")

def test():
    logging.debug('test')


if __name__ == '__main__':
    logging.debug('main test')
    test()
