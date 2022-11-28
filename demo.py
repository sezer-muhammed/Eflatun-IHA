from EflatunIHA.utils import logger, common, label
from EflatunIHA.utils import constants as ct

from pathlib import Path
from PIL import Image
import cv2
import glob

from EflatunIHA.cmd_tools import download_example

test_logger = logger.EflatunLogger()
test_logger.info("Test Logger'i basarili bir sekilde calisti.\n\n")

data_loader = label.TeknoLabelLoader()

test_logger.info(f"Data Loader: {data_loader}")

images_path = glob.glob("eflatun_iha_test_datas/**.jpg", recursive=True)

for image_path in images_path:

    label_path = Path(rf"{image_path.split('.jpg')[0]}.txt")
    img_path = Path(rf"{image_path}")

    image = cv2.imread(str(img_path))

    example_data = data_loader(label_path, ct.TEKNOLABEL_CLASSES_DOUBLE_UAV_NONUAV, img_path, ct.TEKNOLABEL_TYPE_YOLO)

    ground_truth = example_data.get_data()

    for ground_truth_data in ground_truth:
        print(ground_truth_data)
        cv2.rectangle(image, (ground_truth_data[0], ground_truth_data[1]), (ground_truth_data[2], ground_truth_data[3]), (0, 255, 0), 2)
        cv2.putText(image, ground_truth_data[-1], (ground_truth_data[0], ground_truth_data[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow("image", image)
        cv2.waitKey(10)

    test_logger.info("Test basarili bir sekilde tamamlandi.", f"Bulunan Labellar: {example_data}", f"Resim: '{img_path}'")
    test_logger.space()