# Web-Crawler 🕷️
This script will help you to crawl through websites recursively and download files as per your requirement(pdf, docx, ppt, etc.)

<br/>

<p align="center">
  <img src="../assets/jack.jpg?raw=true"/>
  <p align="center">Jack searching for some files ...</p>
</p>
<br/>

## Usage -  
```
 webCrawler.py [-h] [--level LEVEL] [--file_types FILE_TYPES] website_url path
```
```
positional arguments:
  website_url               URL from which you want to download files
  path                      Path to which you want to dump downloaded files

optional arguments:
  -h, --help                show this help message and exit
  --level LEVEL             Level of recursively visiting pages from a link,
                            default = 3
  --file_types FILE_TYPES   Specify comma seperated filetypes such as pdf,txt to
                            be downloaded, default is pdf
                        

```

## Example -
```
 python webCrawler.py --level 4 --file_types pdfg,txt,xls https://www.mywebsite.com E:/dump
```
In this example, script will download all pdfs,txt files from www.mywebsite.com by recursively visiting 4 pages and will dump downloaded files to E:/dump path.

## Development status -
This project is under development and soon will be completed.