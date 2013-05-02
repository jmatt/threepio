"""

Minimally improved noise for python. Pragmatic, minimal improved logging for python.

* Provides two separate log levels.
* One log level for dependencies and one for the application.
* Improved default format string.

example use:
  threepio.initialize(...)
  from threepio import logger
  # ...
  logger.debug('debugorz')
  logger.info('infoz')

example use:
  woot_logger = threepio.initialize(...,
                                       ...,
                                       global_logger=False)
  woot_logger.debug('W00t!')

"""

from __future__ import absolute_import
import logging
import sys
from . import version

__title__ = 'threepio'
__version__ = version.get_version(form='short')
__author__ = 'J. Matt Peterson'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2013 J. Matt Peterson'


logger = None

VERSION = version.VERSION
version = version.get_version(form='verbose')

LOGGER_NAME = "threepio"
LOG_FILENAME = "./threepio.log"
APP_LOGGING_LEVEL = logging.DEBUG
DEP_LOGGING_LEVEL = logging.INFO

def initialize(logger_name=LOGGER_NAME,
               log_filename=LOG_FILENAME,
               app_logging_level=APP_LOGGING_LEVEL,
               dep_logging_level=DEP_LOGGING_LEVEL,
               global_logger=True):
    """
    Constructs and initializes a `logging.Logger` object.

    Returns :class:`logging.Logger` object.

    :param logger_name: name of the new logger.
    :param log_filename: The log file location :class:`str`.
    :param app_logging_level: The logging level to use for the application.
    :param dep_logging_level: The logging level to use for dependencies.
    :param global_logger: If true set threepio's global logger variable to this logger.
    """
    # setup the logging format.
    format = "%(asctime)s %(name)s-%(levelname)s "\
             + "[%(pathname)s %(lineno)d] %(message)s"
    logging.Formatter(format)

    # Setup the root logging for dependencies, etc.
    logging.basicConfig(
        level=dep_logging_level,
        format=format,
        filename=log_filename,
        filemode='a+')

    # Setup and add separate application logging.
    new_logger = logging.getLogger(logger_name)

    # Set the app logging level.
    new_logger.setLevel(app_logging_level)  # required to get level to apply.

    # Set the global_logger by default.
    if global_logger:
        global logger
        logger = new_logger

    return new_logger
