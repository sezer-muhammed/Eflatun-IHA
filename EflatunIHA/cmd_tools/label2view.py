import argparse

parser = argparse.ArgumentParser(
    description="Draw Labels On The Image Then Save"
)
parser.add_argument("-f", '--infolder', type=str, default=None, help='input folder')
parser.add_argument(
    "-l", '--label', type=str, default=None, help='label type: "pascal" or "yolo"'
)
parser.add_argument(
    "-c", '--classes',
    type=str,
    default=None,
    help='label classes config name: "TCSU" or "TCDUN" or "TCU"'
)
parser.add_argument("-s", '--show', action='store_true', help='show image realtime')
parser.add_argument('--save', action='store_true', help='save images')
parser.add_argument("-r", '--random', action='store_true', help='randomize')

opt = parser.parse_args()

from pathlib import Path
import sys
import os
import cv2
from random import shuffle

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from tek_utils.common import hash_255
from tek_utils import constants as ct
from tek_utils.label import TeknoLabel, TeknoLabelLoader

label_type_mapping = {"yolo": ".txt", "pascal": ".xml"}
label_loader_mapping = {
    "yolo": ct.TEKNOLABEL_TYPE_YOLO,
    "pascal": ct.TEKNOLABEL_TYPE_PASCAL
}

in_fold = opt.infolder
config: str
exec(f"config = ct.{opt.classes}")

label_loader = TeknoLabelLoader()

print(f"Loading {opt.label} labels from {in_fold} folder, {opt.show}")

images = [
    x for x in os.listdir(in_fold)
    if x.endswith((".jpg", ".png", ".JPG", ".PNG"))
]

if opt.random:
    shuffle(images)

for image in images:
    try:
        img_path = os.path.join(in_fold, image)
        label_path = os.path.join(
            in_fold,
            image.replace(".jpg", label_type_mapping[opt.label]).replace(
                ".png", label_type_mapping[opt.label]
            )
        )
        label = label_loader(
            label_path, config, img_path, label_loader_mapping[opt.label]
        )
        frame = cv2.imread(img_path)
        print(f"{label}")

        label_data = label.get_data()

        for l in label_data:
            color = (
                hash_255(l[-1] + "B"), hash_255(l[-1] + "G"), hash_255(l[-1] + "R")
            )
            x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame, l[4], (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 2.5, color, 3
            )

        if opt.show:
            cv2.imshow("frame", cv2.resize(frame, (0, 0), fx=0.5, fy=0.5))
            if cv2.waitKey(500) == ord("q"):
                exit()

        if opt.save:
            Path(os.path.join(in_fold,
                            "labeled_output")).mkdir(parents=True, exist_ok=True)
            cv2.imwrite(os.path.join(in_fold, "labeled_output", image), frame)
    except Exception as e:
        print(f"Error: {e}")
        if opt.save:
            Path(os.path.join(in_fold,
                            "labeled_output")).mkdir(parents=True, exist_ok=True)
            cv2.imwrite(os.path.join(in_fold, "labeled_output", image), cv2.imread(img_path))