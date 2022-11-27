import numpy as np
from pathlib import Path
import os
import sys

try:
    os.system("python3 utils/label.py")
    print("utils label.py")
except:
    pass

try:
    os.system("python3 utils/common.py")
    print("utils common.py")
except:
    pass
