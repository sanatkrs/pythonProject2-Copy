import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='automation.log', format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M: %S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        logger.info("This is my first framework implementation")
        logger.info("This is my first framework implementation2")
        logger.info("This is my first framework implementation3")
        logger.info("This is my first framework implementation4")
        logger.info("This is my first framework implementation5")
        logger.info("This is my first framework implementation6")
        return logging

