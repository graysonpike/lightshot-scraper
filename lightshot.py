# Script to download a given Lightshot image using Beautifulsoup4

import os
import shutil
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

LIGHTSHOT_URL = "https://prnt.sc/"
HEADERS = {
	"User-Agent": UserAgent().random
}


def download_image(id, filename):
	page = requests.get(LIGHTSHOT_URL + id, headers=HEADERS)
	soup = BeautifulSoup(page.text, 'html.parser')

	img_url = soup.find("img", attrs={"class": "screenshot-image"})['src']
	if not "http" in img_url:
		img_url = "http://" + img_url

	image_req = requests.get(img_url, stream=True, headers=HEADERS)
	if image_req.status_code == 200:
		file = open(filename, 'wb')
		image_req.raw.decode_content = True
		shutil.copyfileobj(image_req.raw, file)


def test():
	download_image("aa0001", "test.png")


# test()