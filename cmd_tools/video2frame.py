# split video into frames and save them as images in a folder

import argparse

parser = argparse.ArgumentParser(description="Split video into frames")
parser.add_argument('--infolder', type=str, default=None, help='input folder')
parser.add_argument('--hz', type=float, default=1, help='frame rate (Hz)')

opt = parser.parse_args()

import os
import cv2
import glob
from pathlib import Path

def video2frame(infile, hz):
    infile = Path(infile)

    camera = cv2.VideoCapture(str(infile))
    fps=camera.get(cv2.CAP_PROP_FPS)
    period = round(fps/hz)


