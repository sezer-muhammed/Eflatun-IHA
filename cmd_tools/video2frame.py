# split video into frames and save them as images in a folder

import argparse

parser = argparse.ArgumentParser(description="Split video into frames")
parser.add_argument('--infolder', type=str, default=None, help='input folder')
parser.add_argument('--hz', type=float, default=1, help='frame rate (Hz)')

opt = parser.parse_args()
print(opt.hz)