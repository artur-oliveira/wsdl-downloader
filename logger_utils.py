import logging

logging.basicConfig(level=logging.INFO)


class LoggerFactory:
    @staticmethod
    def get_logger(name):
        return logging.getLogger(name)
