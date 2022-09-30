#!/usr/bin/env python
import asyncio
import functools
import sys
import os
import threading
import httpx


async def download(url):
    try:
        loop = asyncio.get_event_loop()
        print(threading.current_thread().name,url)
        log_file = url.split('/')[-1]
        response = await loop.run_in_executor(None,functools.partial( httpx.get,url))
        open(log_file,'w').write(response.text)
    except Exception as e:
        print(e)

# async def write_log(innput_q):
#     pass
#     # open(log_file,'w').write(response.text)

async def main():
    url = "http://localhost:8000"
    url_files = []
    for i in range(1,11):
        url_files.append(f"{url}/apache_logs_{i:02d}.log")
    
    download_tasks = [asyncio.create_task(download(url)) for url in url_files]

    await asyncio.gather(*download_tasks)
    


if __name__ == '__main__':
    
    asyncio.run(main())