import requests
import os
from PIL import Image


class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"


BASE_URL = "https://www.larvalabs.com/public/images/cryptopunks/"
IMG_PATH = "cryptopunks"
RESIZED_IMG_PATH = "resized"


def download_img(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res
    except requests.HTTPError():
        print(Colors.RED + "HTTP ERROR!" + Colors.LIGHT_GRAY)


def write_img(img_name, img):
    img_file = open(os.path.join(IMG_PATH, img_name), "wb")
    for chunk in img.iter_content(100000):
        img_file.write(chunk)
    img_file.close()
    # resize_img(os.path.join(IMG_PATH, img_name))


def create_dirs():
    os.makedirs(IMG_PATH, exist_ok=True)
    os.makedirs(RESIZED_IMG_PATH, exist_ok=True)


def resize_img(img_path):
    img = Image.open(img_path)
    size = (350, 350)
    resized_img = img.resize(size)
    resized_img.save(os.path.join(
        RESIZED_IMG_PATH, os.path.basename(img_path)))


def download_ugly_imgs():
    counter = 1
    while counter < 10:
        img_name = "punk" + str(counter).zfill(4) + ".png"
        print(Colors.GREEN + "Downloading: {}".format(img_name) + Colors.LIGHT_GRAY)
        url = BASE_URL + "/" + img_name
        img = download_img(url)
        write_img(img_name, img)
        counter += 1
    print(Colors.GREEN + "DONE" + Colors.LIGHT_GRAY)


if __name__ == "__main__":
    create_dirs()
    download_ugly_imgs()
