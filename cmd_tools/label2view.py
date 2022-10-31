import argparse

parser = argparse.ArgumentParser(description="Draw Labels On The Image Then Save")
parser.add_argument('--infolder', type=str, default=None, help='input folder')
parser.add_argument('--label', type=str, default=None, help='label type: "pascal" or "yolo"')
parser.add_argument('--classes', type=str, default=None, help='label classes config name')

opt = parser.parse_args()

from pathlib import Path
import sys
import os
import cv2

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from utils.common import load_pascal, load_yolo
from utils import constants as ct

config = None
exec(f"config = ct.{opt.classes}")

print(f"{config} is the config")

in_fold = opt.infolder
out_fold = "_labeled_images"

if opt.label == "pascal":
    load_func = load_pascal
    ext = ".xml"
elif opt.label == "yolo":
    load_func = load_yolo
    ext = ".txt"
else:
    Exception("Label type not supported")

images = [x for x in os.listdir(in_fold) if x.endswith((".jpg", ".png", ".JPG", ".PNG"))]

for image in images:
    img_path = os.path.join(in_fold, image)
    label_path = os.path.join(in_fold, image.replace(".jpg", ext).replace(".png", ext))
    label, w, h = load_func(label_path, img_path=img_path)
    frame = cv2.imread(img_path)
    print(label)

    for l in label:
        x1, y1, x2, y2 = l[0], l[1], l[2], l[3]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, str(l[4]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("frame", cv2.resize(frame, (0, 0), fx=0.5, fy=0.5))
    cv2.waitKey(0)