import argparse
import random
from pathlib import Path
import glob
import shutil
import os

parser = argparse.ArgumentParser(description="Selects random photos from given folder")
parser.add_argument('--infolder', type=str, default=None, help='input folder')
parser.add_argument('--count', type=float, default=1, help='number of photos you want to select')
parser.add_argument('--outfolder', type=str, default=None, help='output folder')
parser.add_argument('--copy', type=str, default=None, help='copy folder')
opt = parser.parse_args()

def photoselector(infile: Path, count: int, outfolder: Path, copyfile: Path):
    
    files = [f for f in infile.iterdir() if f.is_file()]
    randomfiles = random.sample(files, count)
    for f in randomfiles:
        shutil.copy(f, outfolder)
        shutil.move(f, copyfile)

if __name__ == '__main__':
    photoselector(Path(opt.infolder), int(opt.count), Path(opt.outfolder), Path(opt.copy))
    