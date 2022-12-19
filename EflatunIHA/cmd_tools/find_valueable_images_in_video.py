import argparse

parser = argparse.ArgumentParser(
    description="Find valuable images in video and save them"
)
parser.add_argument('--infolder', type=str, default=None, help='input folder with videos')
parser.add_argument('--show', action='store_true', help='show image realtime')
parser.add_argument("--model", type=str, help="model name")
parser.add_argument("--min_conf", type=float, help="minimum confidence for detection")
parser.add_argument("--max_conf", type=float, help="maximum confidence for detection")
parser.add_argument("--skip", type=int, help="skip frames")
opt = parser.parse_args()

from pathlib import Path
import sys
import os
import cv2
import torch
import numpy as np

#* taken from yolov5 repo
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # EflatunIHA root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

from tek_utils.common import hash_255
from tek_utils import constants as ct
from tek_utils.label import TeknoLabel, TeknoLabelLoader

model = torch.hub.load('ultralytics/yolov5', 'custom', path=opt.model)

video_paths = list(Path(opt.infolder).glob('*.mp4')) + list(Path(opt.infolder).glob('*.avi')) + list(Path(opt.infolder).glob('*.mov')) + list(Path(opt.infolder).glob('*.MP4'))

counter = 0 
skip_counter = 0

Path("valuable_images").mkdir(parents=True, exist_ok=True)

for video_path in video_paths:
    print(video_path)
    cap = cv2.VideoCapture(str(video_path))
    while True:
        counter += 1
        ret, frame = cap.read()
        
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = model(frame_rgb, size=640)
        img = results.render()
        cv2.imshow("frame", cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB))
        cv2.waitKey(1)
        confs = results.xyxy[0].cpu().numpy()[:, 4]
        conf_in_range = np.intersect1d(np.where(confs > opt.min_conf), np.where(confs < opt.max_conf))
        if len(conf_in_range) > 0:
            skip_counter += 1
            skip_counter = skip_counter % opt.skip
            if skip_counter == 0:
                cv2.imwrite("valuable_images/" + str(counter) + ".jpg", frame)