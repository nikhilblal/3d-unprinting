import datetime
import os
import sys
import argparse
import math
import json

import cv2
import numpy as np


def main():
    filename_grid = "data/grid.png"
    filename_config = "config.json"

    img = cv2.imread(filename_grid)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    with open(filename_config, "r") as f:
        config = json.load(f)


    m = config["grid"]["rows"]
    n = config["grid"]["columns"]
    s = config["grid"]["size_mm"]

    ret, corners = cv2.findChessboardCorners(img_gray, (m, n), None)

    # img = cv2.drawChessboardCorners(img, (m, n), corners)
    # print(corners)
    # print(ret)


if __name__ == "__main__":
    main()
