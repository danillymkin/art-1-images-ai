from tkinter import *
from PIL import Image
import numpy as np

from GUI import GUI

import os

from NetworkART import NetworkART


def run_art(vectors, P, L):
    art = NetworkART(vectors[0], P, L)
    vector_groups = [1]

    for i, vector in enumerate(vectors[1:]):
        group_num = art.recognition(vector)
        vector_groups.append(group_num)

    print(vector_groups)
    return vector_groups


def get_images(path):
    return [Image.open(path + file_name).resize((32, 32)) for file_name in os.listdir(path)]


def binarize_images(images, softness_white):
    bin_images = []
    for image in images:
        bin_image = image.convert('L')
        bin_image = bin_image.point(lambda p: 255 if p > softness_white else 0)
        bin_images.append(bin_image.convert('1'))
    return bin_images


def show_bin_images():
    try:
        softness_white = int(gui.softness_white.get())
    except ValueError:
        softness_white = 0
    bin_images = binarize_images(raw_images, softness_white)
    gui.show_bin_images(bin_images)
    return bin_images


def on_change(var, index, mode):
    bin_images = show_bin_images()
    image_vectors = [np.asarray(bin_img, dtype=int).flatten() for bin_img in bin_images]
    try:
        P = float(gui.threshold_value.get())
    except ValueError:
        P = 0
    groups = run_art(image_vectors, P, 2)
    gui.clear_art_groups()
    gui.show_art_groups(groups, raw_images)


if __name__ == '__main__':
    gui = GUI('1000x600', 'ART-1')

    raw_images = get_images('images/ARTicon32/')
    gui.show_raw_images(raw_images)

    bin_images = show_bin_images()

    gui.softness_white.trace_add('write', on_change)
    gui.threshold_value.trace_add('write', on_change)

    gui.mainloop()
