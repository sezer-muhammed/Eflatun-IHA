from pathlib import Path
import sys
import os
import time
import numpy as np
from typing import Optional, Tuple, Dict

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from utils.common import load_pascal, save_np2coco, save_np2pascal, save_np2yolo, load_coco, load_yolo
from utils import constants as ct


class TeknoLabel():
    def __init__(self) -> None:
        """Provides label management, supports Pascal VOC (.xml), coco (.json), yolo (.txt) file types to save and np.ndarray to upload

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """

        self.width = None
        self.height = None
        self._label_data = np.empty((0, 6))
        self._label_data_id = np.empty((0, 6))
        self._classes = None

        #* Flags
        self.is_suitable_training = ct.TEKNOLABEL_TRAINABLE_NAN
        self.count_of_label = self._label_data.shape[0]
        self.biggest_object_index = None

    def __str__(self) -> str:
        """Turns the output to a string.

        Returns:
            str: Returns a string to be logged.
        """

        log_message = f"""
Label Data:
{self._label_data}

Label Data Classes: {self._classes}
        """

        return log_message

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
        return self.get_data()

    def analyse(self):
        """Analyses the given dataset while the UAV on the ground
        """

    def analyse_on_flight(self):
        """Analyses the given dataset while the UAV is flying
        """

    def to_pascal(self, out_file: Path, img_path: Path = None):
        """Saves the labels in Pascal VOC (.xml) format to specified file

        Args:
            out_file (Path): Is the result of this method which will be saved into the given path

        Raises:
            TypeError: Implies that the dimensions of the image is given in the wrong format or not given at all.
        """
        if img_path is None:
            raise TypeError("specify image path for the label.")

        if self.width is None or self.height is None:
            raise TypeError("specify width and height of the image.")

        if isinstance(out_file, str):  # Exception handling
            out_file = Path(out_file)

        if isinstance(out_file, Path):
            save_np2pascal(
                data=self._label_data,
                out_file=out_file,
                img_path=img_path,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def to_coco(self, out_file: Path, img_path: Path = None):
        """Converts the np.ndarray to coco (.json) file and save it to the given path

        Args:
            out_file (Path): Is the result of this method which will be saved into the given path

        Raises:
            TypeError: Implies that the dimensions of the image is given in the wrong format or not given at all.
        """
        if img_path is None:
            raise TypeError("specify image path for the label.")

        if self.width is None or self.height is None:
            raise TypeError("specify width and height of the image.")

        if isinstance(out_file, str):  # Exception handling
            out_file = Path(out_file)

        if isinstance(out_file, Path):
            save_np2coco(
                data=self._label_data,
                out_file=out_file,
                img_path=img_path,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def to_yolo(self, out_file: Path, img_path: Path = None):
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
                data=self._label_data_id,
                out_file=out_file,
                img_path=img_path,
                shape=(self.width, self.height)
            )
        else:
            raise TypeError("please input 'Path' object")

    def update(
        self,
        in_array: Optional[np.ndarray] = None,
        shape: Optional[Tuple[int, int]] = None,
        classes: Dict[str, int] = None
    ) -> None:
        """Updates the dataset from the given array

        Args:
            in_array (Optional[np.ndarray], optional): Input numpy array. Defaults to None.
            shape (Optional[Tuple[int, int]], optional): describes the shape of the array. Defaults to None.
            classes (Dict[str,int], optional): Matches the class string with an integer in a dictionary.
            Defaults to None.
        """

        if shape is not None:
            self._update_shape(shape)

        if classes is not None:
            self._classes = classes

        if in_array is not None:

            self._classes = classes
            self._inv_classes = {v: k for k, v in self._classes.items()}

            self._id2text(in_array)
            self._text2id(in_array)

            if shape is not None:
                self._update_shape(shape)
            else:
                self.width = None
                self.height = None

    def _text2id(self, in_array):
        try:
            self._label_data_id = in_array.copy()
            for label in self._label_data_id:
                label_id = self._classes[label[5]]
                label[5] = label_id
        except:
            self._label_data_id = in_array

    def _id2text(self, in_array):
        try:
            self._label_data = in_array.copy()
            for label in self._label_data:
                label_id = self._inv_classes[label[5]]
                label[5] = label_id
        except:
            self._label_data = in_array

    def get_data(self) -> np.ndarray:
        """Returns the loaded data to np.ndarray

        Returns:
            np.ndarray: Returns an n-dimesnional numpy array.
        """

        return self._label_data

    def _update_shape(self, shape: Tuple[int, int]):

        self.width = shape[0]
        self.height = shape[1]


class TeknoLabelLoader():
    def __init__(self) -> None:
        """Initilizes the TeknoLabelLoader class

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.
        """
        self.label_path = None
        self.time_stamp = None
        self.label_type = None

    def __call__(
        self,
        in_file: Path,
        classes: Dict[str, int],
        in_img: Path = None,
        label_type: int = None
    ) -> TeknoLabel:
        """Calls the load() method from the TeknoLabel class

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        return self.load(in_file, classes, in_img, label_type)

    def __str__(self) -> str:
        """Turns the output to a string.

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            str: Returns a string to be logged.
        """

        log_message = f"""
{"Label Path"}: {self.label_path}
{"Access Time"}: {self.time_stamp}
{"Label Type"}: {ct.TEKNOLABEL_TYPES[self.label_type]}
                        """

        return log_message

    def load(
        self,
        in_file: Path,
        classes: Dict[str, int],
        in_img: Path = None,
        label_type: int = None
    ) -> TeknoLabel:
        """Loads the files in the given path

        Args:
            in_file (Path): Is the input of this method which is the data in the given path
            label_type (int, optional): An integer in constants.py file which defines the type of the label

        Raises:
            TypeError: Specify the label type

        Returns:
            TeknoLabel: The class provides label management service.
        """

    def _pascal_load(self, in_file: Path) -> TeknoLabel:
        if isinstance(in_file, str):  # Exception handling
            in_file = Path(in_file)

        if isinstance(in_img, str):  # Exception handling
            in_img = Path(in_img)

        if label_type == ct.TEKNOLABEL_TYPE_COCO:
            np_data, width, height = self._coco_load(in_file, in_img)

        elif label_type == ct.TEKNOLABEL_TYPE_YOLO:
            np_data, width, height = self._yolo_load(in_file, in_img)

        elif label_type == ct.TEKNOLABEL_TYPE_PASCAL:
            np_data, width, height = self._xml_load(in_file, in_img)

        else:
            raise TypeError("Specify the label type")

        temp_tekno_label = TeknoLabel()
        temp_tekno_label.update(
            in_array=np_data, shape=(width, height), classes=classes
        )

        self.label_path = in_file
        self.time_stamp = time.asctime()  #TODO Check if the is correct
        self.label_type = label_type

        return temp_tekno_label

    def _xml_load(self, in_file: Path, in_img: Path = None) -> TeknoLabel:
        """Provides the Pascal VOC (.xml) file load

        Args:
            in_file (Path): Is the input of this method which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """

        return load_pascal(in_file, in_img)

    def _coco_load(self, in_file: Path, in_img: Path = None) -> TeknoLabel:
        """Provides the coco (.json) file load

        Args:
            in_file (Path): Is the input of this method which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        return load_coco(in_file, in_img)

    def _yolo_load(self, in_file: Path, in_img: Path) -> TeknoLabel:
        """Provides the yolo (.txt) file load

        Args:
            in_file (Path): Is the input of this method 
            which is the data in the given path

        Raises:
            NotImplementedError: Implies that this function is not implemented yet.

        Returns:
            TeknoLabel: The class provides label management service.
        """
        return load_yolo(in_file, in_img)


if __name__ == "__main__":
    """
    TeknoLabel and TeknoLabelLoader Tester
    """
    fake_np_array = np.array(
        [[0, 0, 500, 500, 0.54, "uav"], [10, 40, 900, 120, 0.2, "uav"]], object
    )
    fake_np_array_id = np.array(
        [[0, 0, 500, 500, 0.54, 0], [10, 40, 900, 120, 0.2, 0]], object
    )
    fake_shape = (3000, 1500)
    fake_path_pascal = Path("temp/label_saver.xml")
    fake_path_yolo = Path("temp/label_saver.txt")
    fake_img = Path("fakeimg.jpg")

    tester_teknolabel = TeknoLabel()

    tester_teknolabel.update(
        fake_np_array_id, fake_shape, ct.TEKNOLABEL_CLASSES_SINGLE_UAV
    )
    tester_teknolabel.update(
        fake_np_array, fake_shape, ct.TEKNOLABEL_CLASSES_SINGLE_UAV
    )

    tester_teknolabel.get_data()

    print(tester_teknolabel)

    tester_teknolabel.to_pascal(
        Path("temp/teknolabel/pascal.xml"), Path("test.jpg")
    )
    tester_teknolabel.to_yolo(
        Path("temp/teknolabel/yolo.txt"), Path("test.jpg")
    )

    print(tester_teknolabel)

    tester_teknolabel_loader = TeknoLabelLoader()
    tester_teknolabel_loader(
        fake_path_pascal, ct.TEKNOLABEL_CLASSES_SINGLE_UAV, fake_img,
        ct.TEKNOLABEL_TYPE_PASCAL
    )
    print(tester_teknolabel_loader)
