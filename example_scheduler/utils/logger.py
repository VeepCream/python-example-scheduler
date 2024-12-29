import logging.config
from example_scheduler.config import LOG_LEVEL

def get_logger(name='example-scheduler'):
    logging_config = dict(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'standard': {
                    'format': '%(asctime)s %(threadName)s [%(levelname)s] '
                              '%(name)s %(funcName)s [%(lineno)d]: %(message)s'
                },
            },
            'handlers': {
                'default': {
                    'level': LOG_LEVEL,
                    'formatter': 'standard',
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': LOG_LEVEL,
                    'propagate': True
                },
            }
        }
    )
    logging.config.dictConfig(logging_config)
    return logging.getLogger(name)
