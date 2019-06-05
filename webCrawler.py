import sys
import os
import argparse
import traceback
import time
import random
from urllib import request
from bs4 import BeautifulSoup
import shutil

to_be_visited = []
visited_links = {}
downloaded_links = []


def fetch_n_crawl_urls(url, path, max_level, file_types):
    print(url.split("//")[1])
    if not os.path.exists(path):
        os.makedirs(path)
    if url.startswith("http"):
        site_name = url.split('//')[1].replace('www.', '')
    # if site_name.startswith('www.'):
    #     site_name = site_name.replace('www.', '')
    print('---------------------------------------------------------------------')
    print(site_name)
    print('---------------------------------------------------------------------')
    dump_path = path+'/'+site_name
    if not os.path.exists(dump_path):
        os.makedirs(dump_path)
    visited_links[url] = False
    crawler(url, url, dump_path, file_types, 1, max_level)


def crawler(main_url, local_url, path, file_types, current_level, max_level):
    """
    Crawler method is used to crawl through given URL
    up to given level and download specified files
    :param main_url: base URL of website
    :param local_url: URL to be crawled
    :param path: dumping location for downloaded files
    :param file_types: types of files to be downloaded
    :param current_level: current level of web page visit
    :param max_level: level of depth to visit links
    """
    print('crawler called')
    file_type_list = file_types.split(',')
    try:
        if not visited_links[local_url]:
            print('not visited -' + local_url)
            if current_level > max_level:
                print('don"t cross your level-', current_level, ', returning')
                return
            visited_links[local_url] = True
            time.sleep(random.randint(1, 5))  # sleep call so as not to overload the server
            print('visiting--', local_url)
            print('level--', current_level)
            html = request.urlopen(local_url)
            if html.status == 200:
                soup = BeautifulSoup(html, "lxml")
                print('getting links')
                links = soup.find_all('a', recursive=True)
                fetched_links = 0
                for l in links:
                    n_url = l.get('href')
                    if n_url is not None:
                        for file_ext in file_type_list:
                            if n_url.endswith(file_ext):
                                print('lets download--', n_url)
                                if main_url.startswith('https') or main_url.startswith('http'):
                                    if n_url not in downloaded_links:
                                        time.sleep(random.randint(1, 4))   # waiting before accessing URL
                                        res = request.urlopen(main_url + '/' + n_url)
                                        downloaded_links.append(n_url)
                                        visited_links[n_url] = True
                                        print(n_url.split('/')[-1], 'status-', res.status, 'downloading level-', current_level)
                                        with open(path + '/' + n_url.split('/')[-1], 'wb') as f:
                                            shutil.copyfileobj(res, f)
                                fetched_links += 1
                        crawler(main_url, local_url, path, current_level + 1, max_level)

                print("Total files downloaded - ", fetched_links)

    except Exception as e:
        print('Exception in Crawler-', traceback.format_exc())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('website_url', help='URL from which you want to download files')
    parser.add_argument('path', help='Path to which you want to dump downloaded files')
    parser.add_argument('--level', help='Level of recursively visiting pages from a link, default = 3', type=int, default=3)
    parser.add_argument('--file_types', help='Specify comma seperated filetypes such as pdf,txt to be downloaded, default is pdf', default='pdf')
    args = parser.parse_args()

    print('url-', args.website_url)
    print('path-', args.path)
    print('level-', args.level)
    print('filetypes-', args.file_types)
    fetch_n_crawl_urls(args.website_url, args.path, args.level, args.file_types)
