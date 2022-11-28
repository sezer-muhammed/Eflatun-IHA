from pathlib import Path
import sys
import os
from datetime import datetime
from typing import Callable
import logging

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from utils import constants as ct

creation_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOGFILE = ROOT.joinpath(Path(f"logs/{creation_time}_Eflatun.log"))
LOGFILE.parent.mkdir(exist_ok=True, parents=True)
logging.basicConfig(
    filename=LOGFILE, format='[%(levelname)-10s: %(asctime)s] %(message)s'
)


class EflatunLogger():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    def function_logger(self, fucn: Callable, *args):
        """Runs the function and logs the input and outpus of it.

        Args:
            fucn ([Callable]): [Function to be tested]

        Returns:
            [Output of fucn]
        """
        try:
            self.logger.info(f"{fucn.__name__} is called with args: {args}")
            output = fucn(*args)
            self.logger.info(f"{fucn.__name__} is finished. Output: {output}")
            return output
        except Exception as e:
            self.logger.warning(f"{fucn.__name__} is failed. Error: {e}")

    def space(self):
        self.logger.info("")

    def info(self, *args):
        for arg in args:
            self.logger.info(f"{arg}")

    def debug(self, *args):
        for arg in args:
            self.logger.debug(f"{arg}")

    def warning(self, *args):
        for arg in args:
            self.logger.warning(f"{arg}")

    def error(self, *args):
        for arg in args:
            self.logger.error(f"{arg}")

    def critical(self, *args):
        for arg in args:
            self.logger.critical(f"{arg}")


if __name__ == "__main__":
    logger = EflatunLogger()
    logger.info("Logger is testing itself.")

    def test_func(a, b, c):
        return a + b

    test = "Muhammed Izzet Sezer <3 Sevval Dikkaya"

    logger.space()

    try:
        logger.info(test, "True love")
        logger.info("logger is working.")
    except:
        logger.warning("logger is not working.")

    logger.space()

    try:
        logger.function_logger(test_func, 60, 5, "milyon")
        logger.info("function_logger is working.")
    except:
        logger.warning("function_logger is not working.")

    logger.space()

    try:
        logger.function_logger(test_func, 60, 5, "milyon", 5)
        logger.info("function_logger error is passed.")
    except:
        logger.warning("function_logger is not working.")
