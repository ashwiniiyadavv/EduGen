import logging
import logging.config

# Load the configuration from the file
logging.config.fileConfig('logger/logging.conf')

# Get a logger
logger = logging.getLogger(__name__)

