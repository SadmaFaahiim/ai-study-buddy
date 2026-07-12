import logging
import os
import sys

def setup_logger(name: str = "ai_learning_buddy") -> logging.Logger:
    """
    Sets up a consolidated logger with custom console handlers and formatting.
    
    Args:
        name: Name of the logger instance.
        
    Returns:
        A configured logging.Logger instance.
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers if setup_logger is called multiple times
    if logger.handlers:
        return logger

    # Retrieve log level from env, default to INFO
    log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(log_level)

    # Format config: Date Time | Level | Message
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler (Stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.propagate = False
    return logger

# Single instance for the application
logger = setup_logger()
