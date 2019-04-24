import sys
import argparse

def fetch_n_crawl_urls(url, path):
	print('fetching...')


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='URL from which you want to download files')
	parser.add_argument('path', help='Path to which you want to dump downloaded files')
	parser.add_argument('--level', help='Level of recursively visiting pages from a link, default = 3', type=int, default=3)
	parser.add_argument('--filetypes', help='Specify comma seperated filetypes such as pdf,txt to be downloaded, default is pdf', default='pdf')
	args = parser.parse_args()

	print('url-', args.url)
	print('path-', args.path)
	print('level-', args.level)
	print('filetypes-', args.filetypes)
	# print(sys.argv)
	# url = sys.argv[1]
	# file_path = sys.argv[2]
	# print('Data will be downloaded from-', url)
	# print('Documents will be stored at-', file_path)
	# fetch_n_crawl_urls(url, file_path)
