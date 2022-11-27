import argparse

parser = argparse.ArgumentParser(description="Split video into frames")
parser.add_argument('--infolder', type=str, default=None, help='input folder')
parser.add_argument('--hz', type=float, default=1, help='frame rate (Hz)')

opt = parser.parse_args()

import os
import cv2
import glob
from pathlib import Path


def video2frame(infile: Path, hz: float, outfile: Path):

    camera = cv2.VideoCapture(str(infile))

    counter = 0

    fps = camera.get(cv2.CAP_PROP_FPS)
    period = round(fps / hz)
    print(f"Starting operation with {fps} fps and {hz} Hz, {infile}")

    while True:
        counter += 1

        camera.set(cv2.CAP_PROP_POS_FRAMES, (counter * period) - 1)
        ret, frame = camera.read()

        if ret is False:
            break

        outfile.mkdir(parents=True, exist_ok=True)

        frame_name = f"{period}_{counter}_{infile.stem}_teknofest2023.jpg"

        full_path = os.path.join(outfile, frame_name)

        cv2.imwrite(full_path, frame)
        print(f"Frame {counter} saved", end="\r")


videos = glob.glob(opt.infolder + "/**.*", recursive=True)

for video in videos:
    if video.endswith((".mp4", ".mov", ".MP4", ".MOV")):
        video2frame(Path(video), opt.hz, Path("frames"))
