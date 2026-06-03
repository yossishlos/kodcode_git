import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)

format = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s |")

filehandler = logging.FileHandler("system.log")

filehandler.setFormatter(format)
logger.addHandler(filehandler)
streamhandler = logging.StreamHandler()
streamhandler.setFormatter(format)
logger.addHandler(streamhandler)


logger.info("testing")