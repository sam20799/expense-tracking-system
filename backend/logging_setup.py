import logging
from pathlib import Path

def log_setup(file_name,log_file='server.log'):
    log_file_path = Path(__file__).parent / log_file

    logger = logging.getLogger(file_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger