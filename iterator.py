import os
from lightshot import download_image


OUTPUT_DIR = "output"


def main():

	completed_ids = [x.replace('.png', '') for x in os.listdir(OUTPUT_DIR)]

	for id_num in range(1, 100000):
		last_4 = "%04d" % (id_num % 10000)
		first_2_dec = id_num // 10000
		first_2 = chr(ord('a') + first_2_dec // 26) + chr(ord('a') + first_2_dec % 26)
		id_str = first_2 + last_4
		if not id_str in completed_ids:
			download_image(id_str, os.path.join(OUTPUT_DIR, id_str + '.png'))


main()
