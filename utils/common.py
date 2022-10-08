import numpy as np
from pascal_voc_writer import Writer
from pathlib import Path
from typing import Tuple
import os


def save_np2pascal(
    data: np.ndarray, out_file: Path, img_path: Path, shape: Tuple[int, int]
):
    """AI is creating summary for save_np2pascal

    Args:
        data (np.ndarray): [description]
        out_file (Path): [description]
        img_path (Path): [description]
        shape (Tuple[int, int]): [description]
    """

    out_dir = Path(os.path.dirname(out_file))
    out_dir.mkdir(exist_ok=True, parents=True)

    pascal_writer = Writer(img_path, shape[0], shape[1])

    for label in data:

        pascal_writer.addObject(
            label[5], label[0], label[1], label[2], label[3]
        )

    pascal_writer.save(out_file)


def save_np2coco(
    data: np.ndarray, out_file: Path, img_path: Path, shape: Tuple[int, int]
):

    raise NotImplementedError("This method is not implemented yet.")


def save_np2yolo(
    data: np.ndarray, out_file: Path, img_path: Path, shape: Tuple[int, int]
):
    """AI is creating summary for save_np2yolo

    Args:
        data (np.ndarray): [description]
        out_file (Path): [description]
        img_path (Path): [description]
        shape (Tuple[int, int]): [description]
    """

    out_dir = Path(os.path.dirname(out_file))
    out_dir.mkdir(exist_ok=True, parents=True)

    yolo_file = open(out_file, "w")

    for label in data:

        x_center = ((label[0] + label[2]) / 2) / shape[0]
        y_center = ((label[1] + label[3]) / 2) / shape[1]

        x_width = (label[2] - label[0]) / shape[0]
        y_width = (label[3] - label[1]) / shape[1]

        line = f"{int(label[5])} {x_center} {y_center} {x_width} {y_width}\n"

        yolo_file.write(line)

    yolo_file.close()


def load_yolo():
    raise NotImplementedError("This method is not implemented yet.")


def load_coco():
    raise NotImplementedError("This method is not implemented yet.")


def load_pascal():
    raise NotImplementedError("This method is not implemented yet.")


if __name__ == "__main__":
    """
    Commons tester codes
    """

    fake_np_array = np.array(
        [[0, 0, 500, 500, 0.54, "Bus"], [10, 40, 900, 120, 0.2, "IHA"]]
    )
    fake_np_array_id = np.array(
        [[0, 0, 500, 500, 0.54, 0], [10, 40, 900, 120, 0.2, 1]]
    )
    fake_shape = (3000, 1500)
    fake_path_pascal = Path("temp/label_saver.xml")
    fake_path_yolo = Path("temp/label_saver.txt")
    fake_img = Path("fakeimg.jpg")

    save_np2pascal(fake_np_array, fake_path_pascal, fake_img, fake_shape)
    save_np2yolo(fake_np_array_id, fake_path_yolo, fake_img, fake_shape)
    #save_np2coco(fake_np_array, fake_path, fake_img, fake_shape)
