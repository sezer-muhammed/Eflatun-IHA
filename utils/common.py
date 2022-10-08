import numpy as np
import pascal_voc_writer
from pathlib import Path
from typing import Tuple


def save_np2pascal(data: np.ndarray, out_file: Path, shape: Tuple[int, int]):
    raise NotImplementedError("This method is not implemented yet.")


def save_np2coco(data: np.ndarray, out_file: Path, shape: Tuple[int, int]):
    raise NotImplementedError("This method is not implemented yet.")


def save_np2yolo(data: np.ndarray, out_file: Path, shape: Tuple[int, int]):
    raise NotImplementedError("This method is not implemented yet.")


def load_yolo():
    raise NotImplementedError("This method is not implemented yet.")


def load_coco():
    raise NotImplementedError("This method is not implemented yet.")


def load_pascal():
    raise NotImplementedError("This method is not implemented yet.")
