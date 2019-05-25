# Web-Crawler
This script will help you to crawl through websites recursively and download files as per your requirement(pdf, docx, ppt, etc.)

<br/>

<p align="center">
  <img src="../assets/jack.jpg?raw=true"></img>
</p>
<br/>

## Usage:  
```
python webCrawler.py [-h] [--level LEVEL] url path
```
```
positional arguments:
  url            URL from which you want to download files
  path           Path to which you want to dump downloaded files

optional arguments:
  -h, --help     show this help message and exit
  --level LEVEL  Level of recursively visiting pages from a link, default is 3
```

## Example -
 <br/>
```
 python webCrawler.py --level 4 www.mywebsite.com E:/dump
```
In this example, script will download files from www.mywebsite.com by recursively visiting 4 pages and will dump downloaded files to E:/dump path.

## Development status -
This project is under development and soon will be completed.