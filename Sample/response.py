import time
import logging

class SubmissionResponse:
    def __init__(self, subreddit="", url="", title="", count=0, delay=600, output="output.log"):
        self.subreddit = subreddit
        self.url = url
        self.title = title
        self.count = count
        self.delay = delay

        self.logger = self.setup_logger(output)

    def success(self):
        self.count += 1
        self.logger.info("'{0}' - '{1}' - '{2}'".format(self.subreddit, self.title, self.url))

    def failure(self, message):
        self.logger.error("'{0}' - '{1}' - '{2}' - '{3}'".format(self.subreddit, self.title, self.url, message))
        print("Praw API policy for stream data: Delay 10 minutes to accept a new submission.")
        time.sleep(self.delay)


    def setup_logger(self, output_path):
        # Create the Logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Debug for duplicity (Logger is Singleton)
        if (logger.hasHandlers()):
            logger.handlers.clear()

        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler(output_path)
        logger_handler.setLevel(logging.DEBUG)

        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',  datefmt='%d-%m-%Y %H:%M:%S')

        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

        # Add the Handler to the Logger
        logger.addHandler(logger_handler)
        return logger
