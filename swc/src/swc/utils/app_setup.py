from future import standard_library

standard_library.install_aliases()

import logging
from logging.handlers import RotatingFileHandler
import builtins
import json
import os


def setup_logging(app):
    """
    It sets logging app.configuration.

    :param app: Application context.
    :type app: object
    """
    # Configure logging
    formatter = logging.Formatter(app.config['LOG_MSG_FORMAT'])
    # Debug Log
    if app.config['DEBUG']:
        debug_handler = RotatingFileHandler(app.config['DEBUG_LOG_FILE'],
                                            maxBytes=app.config['LOG_FILE_SIZE'],
                                            backupCount=app.config['LOG_FILE_COUNT'])
        debug_handler.setLevel(logging.DEBUG)
        debug_handler.setFormatter(formatter)
        app.logger.addHandler(debug_handler)
    # Error Log
    error_file_handler = RotatingFileHandler(app.config['ERROR_LOG_FILE'],
                                             maxBytes=app.config['LOG_FILE_SIZE'],
                                             backupCount=app.config['LOG_FILE_COUNT'])

    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(formatter)
    app.logger.addHandler(error_file_handler)
    # Scheduler logger
    logger = logging.getLogger()
    logger.addHandler(error_file_handler)


def load_conf(app):
    """
    It reads and loads plumber application configuration.

    :returns: configuration dictionary.
    :rtype: dict
    """

    conf_file_name = 'conf'
    if app.environment == 'TESTING':
        conf_file_name = 'conf_testing'

    # Load application configurations
    if app.environment == 'TESTING':
        with open('swc/conf/%s.json' % conf_file_name) as f:
            conf = json.load(f)
            builtins.gpt['config'] = conf

            basedir = os.path.abspath(os.path.dirname(__file__ + "/../../"))

        app.config.update(builtins.gpt['config'])
