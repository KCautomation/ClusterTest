import logging
import logging.config


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\shabr\PycharmProjects\\ClusterTest\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

        # logger.info("*************** Test_001_Login *****************")
        # logger.warning("*************** Test_001_Login *****************")
        # logger.warning("*************** Test_001_Login *****************")
        # logger.warning("*************** Test_001_Login *****************")
