#!/usr/bin/env python
import sys
import os
import httpx

def main():
    url = "http://localhost:8000"
    for i in range(1,11):
        url_file=f"{url}/apache_logs_{i:02d}.log"
        response = httpx.get(url_file)
        open(url_file.split('/')[-1],'w').write(response.text)

if __name__ == '__main__':
    main()