import os
import glob
import numpy as np

STATIC_FOLDER = "static"

def clear_static_folder():
    files = glob.glob(os.path.join(STATIC_FOLDER, "*"))
    for f in files:
        os.remove(f)

def is_greyscale(img):
    if len(img.shape) < 3:
        return True
    if img.shape[2] == 1:
        return True
    b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]
    return np.allclose(b, g) and np.allclose(b, r)
