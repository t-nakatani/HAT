#!/usr/bin/env python

import cv2
import os
import re
import shutil
import sys

args = sys.argv

DIR_NAME = args[1]
img_paths = [os.path.join(DIR_NAME, fname) for fname in os.listdir(DIR_NAME)]
for img_path in img_paths:
    img = cv2.imread(img_path)
    fname = os.path.basename(img_path)
    test_i = re.findall('test_[0-9]+', fname)[0]
    new_fname = f'{test_i}_answer.tif'
    new_path = os.path.join('./submit', new_fname)
    cv2.imwrite(new_path, img)

shutil.make_archive('submit', format='zip', root_dir='./submit')
