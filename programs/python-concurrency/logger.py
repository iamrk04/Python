import logging
import os


def get_logger(name, level=logging.INFO, log_file_path=None, format=None):
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler and set its logging level
    if log_file_path:
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.INFO)

    # Create a console handler and set its logging level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Create formatters and add them to the handlers
    if format is None:
        format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' 
    file_formatter = logging.Formatter(format)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger