import sys


def fetch_n_crawl_urls(url, path):
	print('fetching...')


if __name__ == '__main__':
    print(sys.argv)
    url = sys.argv[1]
    file_path = sys.argv[2]
    print('Data will be downloaded from-', url)
    print('Documents will be stored at-', file_path)
    fetch_n_crawl_urls(url, file_path)
