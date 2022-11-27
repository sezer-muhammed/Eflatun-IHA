from pathlib import Path
import sys
import os
import time
import numpy as np
from datetime import datetime
from typing import Optional, Tuple, Dict, Callable
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
logging.basicConfig(filename=LOGFILE , format='[%(asctime)s: %(levelname)s] %(message)s')

class EflatunLogger():

    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.info("Logger is created.")

    def function_logger(self, fucn: Callable, *args):
        """Runs the function and logs the input and outpus of it.

        Args:
            fucn ([Callable]): [Function to be tested]

        Returns:
            [Output of fucn]
        """
        self.logger.info(f"{fucn.__name__} is called with args: {args}")
        output = fucn(*args)
        self.logger.info(f"{fucn.__name__} is finished. Output: {output}")
        return output

    def variable_logger(self, *args):
        for arg in args:
            self.logger.info(f"{arg}")

if __name__ == "__main__":
    logger = EflatunLogger()

    def test_func(a, b, c):
        return a + b 

    test = 98
    logger.variable_logger(test, "asdsad")
    logger.function_logger(test_func, 1, 2, "asdsadsa")