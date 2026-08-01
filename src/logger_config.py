import logging
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parent.parent / "taskflow.log"

logger = logging.getLogger("TaskFlow")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)