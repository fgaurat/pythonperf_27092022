#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
import sys
import os
import threading
import httpx

def download(url):
    print(threading.current_thread().name,url)
    log_file = url.split('/')[-1]
    response = httpx.get(url)
    open(log_file,'w').write(response.text)

def main():
    url = "http://localhost:8000"

    url_files = []
    for i in range(1,11):
        url_files.append(f"{url}/apache_logs_{i:02d}.log")

    with ThreadPool(10) as p:
        p.map(download, url_files)


if __name__ == '__main__':
    main()