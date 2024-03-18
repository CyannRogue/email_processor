# logger.py

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging(base_dir_path):
    log_dir = base_dir_path / "Logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "script.log"

    logger = logging.getLogger("EmailExtraction")
    handler = RotatingFileHandler(log_file, maxBytes=5000000, backupCount=5)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger
