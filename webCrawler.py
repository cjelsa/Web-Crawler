import sys
import os
import argparse

to_be_visited = []
visited_links = {}
downloaded_links = []


def fetch_n_crawl_urls(url, path, level, filetypes):
    if not os.path.exists(path):
        os.makedirs(path)
    site_name = url.split('//')[1].replace('/', '', 3)
    if site_name.startswith('www.'):
        site_name = site_name.replace('www.', '')
    print('---------------------------------------------------------------------')
    print(site_name)
    print('---------------------------------------------------------------------')
    dump_path = path+'/'+site_name
    if not os.path.exists(dump_path):
        os.makedirs(dump_path)
    visited_links[url] = False
    crawler(url, url, dump_path, 1)


def crawler(main_url, local_url, path, level):
    print('crawler called')


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



    fetch_n_crawl_urls(args.url, args.path, args.level, args.filetypes)
