import logging

logger = logging.getLogger("medassist")
handler = logging.StreamHandler()
fmt = logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s")
handler.setFormatter(fmt)
logger.addHandler(handler)
logger.setLevel(logging.INFO)