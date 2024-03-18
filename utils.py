import re
from datetime import datetime
from pathlib import Path

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def log_message(day_dir, message):
    log_dir = day_dir / "Logs"
    log_dir.mkdir(exist_ok=True)
    with open(log_dir / "operation_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
