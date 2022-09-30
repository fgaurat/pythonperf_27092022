#!/usr/bin/env python
import sys
import os
import threading
import httpx


def download(url):
    log_file = url.split('/')[-1]
    response = httpx.get(url)
    open(log_file,'w').write(response.text)

def main():
    url = "http://localhost:8000"
    for i in range(1,11):
        url_file=f"{url}/apache_logs_{i:02d}.log"
        threading.Thread(target=download,args=[url_file]).start()

        

if __name__ == '__main__':
    main()