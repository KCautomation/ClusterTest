import logging
import logging.config


class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename="automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.basicConfig(filename="danda.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
