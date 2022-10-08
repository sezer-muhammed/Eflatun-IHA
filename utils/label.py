from pathlib import Path
import sys
import os
import numpy as np


#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative


class TeknoLabel():


    def __init__(self) -> None:
        """Provides label management, supports Pascal VOC (.xml), coco (.json), 
        yolo (.txt) file types to save and np.ndarray to upload

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
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
    def analyse(self):
        """

        :return:
        """
    def analyse_on_flight(self):
        """


        :return:
        """


    def to_xml(self, out_file: Path) -> bool:
        """Saves the labels in Pascal VOC (.xml) format to specified file

        Args:
            out_file (Path): Is the result of this method 
            which will be saved into the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            bool: boolean (1 or 0) to indicate whether process finished succesfully or not
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def to_coco(self, out_file: Path) -> bool:
        """Converts the np.ndarray to coco (.json) file and save it to the given path

        Args:
            out_file (Path): Is the result of this method 
            which will be saved into the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            bool: boolean (1 or 0) to indicate whether process finished succesfully or not
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def to_yolo(self, out_file: Path) -> bool:
        """Converts the np.ndarray to yolo (.txt) file and save it to the given path

        Args:
            out_file (Path): Is the result of this method 
            which will be saved into the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            bool: boolean (1 or 0) to indicate whether process finished succesfully or not
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def update(self, in_file: np.ndarray) -> None:
        """Updates the data that this object holds

        Args:
            in_file (np.ndarray): Is the input of this method 
            which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        raise NotImplementedError("This Code is not implemented yet.")

    def get_data(self) -> np.ndarray:
        """Converts the loaded data to np.ndarray

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            np.ndarray: Returns an n-dimesnional numpy array.
        """
        raise NotImplementedError("This Code is not implemented yet.")


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