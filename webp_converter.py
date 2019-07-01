# coding: utf-8
"""A interactive console script converting a directory of images to Webp format"""
import os.path
import pathlib

import PIL.Image
import tqdm

DEFAULT_OUT_DIR = "out"


def main():
    in_dp = input("input directory: ")
    out_dp = input("output directory [{}]: ".format(DEFAULT_OUT_DIR))
    out_dp = out_dp if out_dp else DEFAULT_OUT_DIR
    os.mkdir(out_dp)
    path = pathlib.Path(in_dp)
    total = len(os.listdir(path))
    index = 0
    for file in tqdm.tqdm(path.iterdir(), total=total):
        try:
            im = PIL.Image.open(file)
        except OSError:
            continue
        fp = os.path.join(out_dp, "{}.webp".format(index))
        im.save(fp)
        index += 1


if __name__ == '__main__':
    main()
