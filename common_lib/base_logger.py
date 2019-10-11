import datetime
import logging


class BaseLogger:
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    @classmethod
    def get_info_log(cls, message):
        """Return datetime and logging message """
        log = '{}: {}'.format(str(datetime.datetime.utcnow()), message)
        print(log)
        return cls.logger.info(log)

    @staticmethod
    def response_logging(response):
        """Parse response and return it to stdout"""
        BaseLogger.get_info_log('Received "{}".'.format(response))
        try:
            parsed_response = response.text
            BaseLogger.get_info_log('Response body "{}".'.format(parsed_response))
        except AttributeError:
            BaseLogger.get_info_log('Response body is empty or cannot by parsed')
