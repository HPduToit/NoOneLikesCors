import logging
import logging.config

logging.config.fileConfig("logging.conf")

log_ume = logging.getLogger("ume")
log_root = logging.getLogger("root")
