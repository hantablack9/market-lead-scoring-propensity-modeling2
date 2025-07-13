import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(LOGS_PATH), exist_ok=True)


LOG_FILE_PATH = os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


# def get_logger(name:str, log_file:str)-> logging.Logger:
#     """
#     Returns a logger configured with file and console handlers
#     :param name: Name of the logger
#     :param log_file: Path to the log file
#     :return: Configured logger instance
#     """

#     # Create a logger for this module
#     os.makedirs('logs', exist_ok=True) # Ensure logs directory exists

#     logger = logging.getLogger(name)
#     logger.setLevel(logging._SysExcInfoType)

#     # Prevent duplicate handlers

#     if not logger.hasHandlers():
#         formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s') # Log format

#         # Create file and stream handlers
#         file_handler = logging.FileHandler(f"logs/{log_file}", mode='a') # Log to file
#         file_handler.setFormatter(formatter)

#         stream_handler = logging.StreamHandler() # Print to console
#         stream_handler.setFormatter(formatter)

#         logger.addHandler(file_handler)
#         logger.addHandler(stream_handler)

#     return logger


# # logging.basicConfig(
# #     level=logging.INFO,
# #     format='[%(asctime)s][%(levelname)s]%(message)s',
# #     handlers=[
# #         logging.FileHandler['src/logging/data_ingestion.log', mode = 'a'],
# #         logging.StreamHandler() # Also print to console
# #         ]
# #     )

# # logger = logging.getLogger(__name__)
