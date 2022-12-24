from EflatunIHA.tek_utils import logger, common, label
from EflatunIHA.tek_utils import constants as ct

from pathlib import Path
from PIL import Image
import cv2
import glob
import os
import shutil

images = glob.glob("*/*.jpg")
loader = label.TeknoLabelLoader()

counter = 0

Path("oturum_data").mkdir(exist_ok=True, parents=True)

for image in images:

    if counter % 4 == 0:
        xml = image.replace(".jpg", ".xml")

        label_data = loader(Path(xml), ct.TEKNOLABEL_CLASSES_ULASIM, Path(image), ct.TEKNOLABEL_TYPE_PASCAL)

        label_data._label_data[label_data._label_data == "Taşıt"] = "car"
        label_data._label_data[label_data._label_data == "İnsan"] = "ins"
        
        label_data._label_data[label_data._label_data == "UAİ"] = "uyam"
        label_data._label_data[label_data._label_data == "UAP"] = "uuap"

        if "uuap" in label_data._label_data:
            continue

        if "uyam" in label_data._label_data:
            continue

        shutil.copy(image, f"oturum_data/{counter}_teknofest_2022_data.jpg")
        label_data.to_pascal(Path(f"oturum_data/{counter}_teknofest_2022_data.xml"), f"oturum_data/{counter}_teknofest_2022_data.jpg")

        print(counter, len(images))

    counter += 1
