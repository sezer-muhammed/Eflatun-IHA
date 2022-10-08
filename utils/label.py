from pathlib import Path
import sys
import os
import numpy as np
from typing import Optional, Tuple

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from utils.common import load_pascal, save_np2coco, save_np2pascal, save_np2yolo
from utils import constants as ct


class TeknoLabel():
    def __init__(self) -> None:
        """Provides label management, supports Pascal VOC (.xml), coco (.json), 
        yolo (.txt) file types to save and np.ndarray to upload

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """

        self.width = None
        self.height = None
        self._label_data = np.empty((0, 6))

        #* Flags
        self.is_suitable_training = ct.TEKNOLABEL_TRAINABLE_NAN
        self.count_of_label = self._label_data.shape[0]
        self.biggest_object_index = None

        raise NotImplementedError("This Code is not implemented yet.")

    def __str__(self) -> str:
        """Turns the output to a string to log.

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            str: Returns a string to be logged.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __add__(self, __o):
        """Combines labels on two TeknoLabel's

        Args:
            __o ([type]): Is the other object which will be combined.

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __sub__(self, __o):
        """Returns the difference of two objects.

        Args:
            __o ([type]): Is the other object which will be subtracted.

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __and__(self, __o):
        """Returns two objects

        Args:
            __o ([type]): Is the other object which will be returned 

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __call__(self) -> np.ndarray:
        """Calls get_data() method

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            np.ndarray: Returns a numpy n-dimensional array
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def analyse(self):  #TODO edit
        """AI is creating summary for analyse
        """

    def analyse_on_flight(self):  #TODO edit
        """AI is creating summary for analyse_on_flight
        """

    def to_pascal(self, out_file: Path):
        """Saves the labels in Pascal VOC (.xml) format to specified file

        Args:
            out_file (Path): Is the result of this method 
            which will be saved into the given path

        Raises:
            TypeError: Implies that the dimensions of the image is given in the wrong format or not given at all.
        """
        if self.width is None or self.height is None:
            raise TypeError("specify width and height of the image.")

        if isinstance(out_file, str):  # Exception handling
            out_file = Path(out_file)

        if isinstance(out_file, Path):
            save_np2pascal(
                data=self._label_data,
                out_file=out_file,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def to_coco(self, out_file: Path):
        """Converts the np.ndarray to coco (.json) file and save it to the given path

        Args:
            out_file (Path): Is the result of this method 
            which will be saved into the given path

        Raises:
            TypeError: Implies that the dimensions of the image is given in the wrong format or not given at all.
        """
        if self.width is None or self.height is None:
            raise TypeError("specify width and height of the image.")

        if isinstance(out_file, str):  # Exception handling
            out_file = Path(out_file)

        if isinstance(out_file, Path):
            save_np2coco(
                data=self._label_data,
                out_file=out_file,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def to_yolo(self, out_file: Path):
        """Converts the np.ndarray to yolo (.txt) file and save it to the given path

        Args:
            out_file (Path): Is the result of this method which will be saved into the given path

        Raises:
            TypeError: Implies that the dimensions of the image is given in the wrong format or not given at all.
        """
        if self.width is None or self.height is None:
            raise TypeError("specify width and height of the image.")

        if isinstance(out_file, str):  # Exception handling
            out_file = Path(out_file)

        if isinstance(out_file, Path):
            save_np2yolo(
                data=self._label_data,
                out_file=out_file,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def update(
        self,
        in_array: Optional[np.ndarray] = None,
        shape: Optional[Tuple[int, int]] = None
    ) -> None:
        """Updates the data that this object holds

        Args:
            in_file (np.ndarray): Is the input of this method 
            which is the data in the given path
        """

        if shape is not None:
            self._update_shape(shape)

        if in_array is not None:
            self._label_data = in_array

            if shape is not None:
                self._update_shape(shape)
            else:
                self.width = None
                self.height = None

    def get_data(self) -> np.ndarray:
        """Returns the loaded data to np.ndarray

        Returns:
            np.ndarray: Returns an n-dimesnional numpy array.
        """
        
        return self._label_data

    def _update_shape(self, shape: Tuple[int, int]):
        """AI is creating summary for _update_shape

        Args:
            shape (Tuple[int,int]): [description]
        """

        self.width = shape[0]
        self.height = shape[1]


class TeknoLabelLoader():
    def __init__(self) -> None:
        """Initilizes the TeknoLabelLoader class

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __call__(self) -> TeknoLabel:
        """Calls the load() method from the TeknoLabel class

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def __str__(self) -> str:
        """Turns the output to a string.

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            str: Returns a string to be logged.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def load(self, in_file: Path, label_type: int) -> TeknoLabel:
        """Loads the files in the given path

        Args:
            in_file (Path): Is the input of this method 
            which is the data in the given path
            label_type (int): An integer in constants.py file 
            which defines the type of the label

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def _xml_load(self, in_file: Path) -> TeknoLabel:
        """Provides the Pascal VOC (.xml) file load

        Args:
            in_file (Path): Is the input of this method 
            which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def _coco_load(self, in_file: Path) -> TeknoLabel:
        """Provides the coco (.json) file load

        Args:
            in_file (Path): Is the input of this method 
            which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def _yolo_load(self, in_file: Path) -> TeknoLabel:
        """Provides the yolo (.txt) file load

        Args:
            in_file (Path): Is the input of this method 
            which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        raise NotImplementedError("This Code is not implemented yet.")

if __name__ == "__main__":
    """
    TeknoLabel and TeknoLabelLoader Tester
    """
