from turtle import width
import numpy as np
from pascal_voc_writer import Writer
from pathlib import Path
from typing import Tuple, List
import os
import cv2

from PIL import Image
import xml.etree.ElementTree as ET

def hash_255(string: str) -> int:
    """Return random number between 0 - 255 from string for color generation

    Args:
        string (str): [The text]

    Returns:
        int: [0 - 255 integer]
    """

    hash = 0
    for counter, i in enumerate(string):
        hash += ord(i) * (counter + 5)
    return hash % 255


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


def load_yolo(in_file: Path, img_path: Path) -> Tuple[np.ndarray, int, int]: #! Fix The code!

    yolo_file = open(in_file, "r")
    data = yolo_file.read()
    yolo_file.close()

    data = data.split("\n")
    data = data[:-1]

    data = [i.split(" ") for i in data]
    data = np.array(data, dtype=np.float32)

    if len(data.shape) == 1:  #shape correction
        data = np.empty((0, 5))

    im = Image.open(img_path)
    width, height = im.size

    x_min = (data[:, 1] - (data[:, 3] / 2)) * width
    y_min = (data[:, 2] - (data[:, 4] / 2)) * height
    x_max = (data[:, 1] + (data[:, 3] / 2)) * width
    y_max = (data[:, 2] + (data[:, 4] / 2)) * height

    data = np.stack((x_min, y_min, x_max, y_max, data[:, 0]), axis=1)

    data = np.array(data, dtype=np.int32)
    return data, width, height


def load_coco(in_file: Path,
              img_path: Path = None) -> Tuple[np.ndarray, int, int]:
    raise NotImplementedError("This method is not implemented yet.")


def load_pascal(in_file: Path,
                img_path: Path = None) -> Tuple[np.ndarray, int, int]:

    tree = ET.parse(in_file, parser=ET.XMLParser(encoding='iso-8859-5'))
    root = tree.getroot()

    width = int(root.find('size').find('width').text)
    height = int(root.find('size').find('height').text)

    list_with_all_boxes = []

    for boxes in root.iter('object'):

        ymin = int(boxes.find("bndbox/ymin").text)
        xmin = int(boxes.find("bndbox/xmin").text)
        ymax = int(boxes.find("bndbox/ymax").text)
        xmax = int(boxes.find("bndbox/xmax").text)
        name = str(boxes.find("name").text)

        list_with_single_boxes = [xmin, ymin, xmax, ymax, name]
        list_with_all_boxes.append(list_with_single_boxes)

    return np.array(list_with_all_boxes, dtype=object), width, height


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

    #fake_np_array_id = np.empty((0,5), int)

    fake_shape = (3000, 1500)
    fake_path_pascal = Path("temp/label_saver.xml")
    fake_path_yolo = Path("temp/label_saver.txt")
    fake_img = Path("temp/fakeimg.jpg")

    cv2.imwrite(str(fake_img), np.zeros(fake_shape + (3, )))

    save_np2pascal(fake_np_array, fake_path_pascal, fake_img, fake_shape)
    save_np2yolo(fake_np_array_id, fake_path_yolo, fake_img, fake_shape)
    #save_np2coco(fake_np_array, fake_path, fake_img, fake_shape)

    load_pascal(Path("temp\label_saver.xml"))
    load_yolo(Path("temp/label_saver.txt"), Path("temp/fakeimg.jpg"))
    #load_coco(Path("temp/label_saver.txt"), Path("temp/fakeimg.jpg"))
