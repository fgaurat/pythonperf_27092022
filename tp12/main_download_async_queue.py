#!/usr/bin/env python
import asyncio
import functools
import sys
import os
import threading
import httpx

async def download(input_q,output_q,worker_id):
    while True:
        data = await input_q.get()
        url = data['url']
        print(threading.current_thread().name,url,worker_id)
        log_file = url.split('/')[-1]
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            output_q.put_nowait({"text":response.text,"url":url})
            input_q.task_done()
    
async def write_log(output_q,worker_id):
    while True:
        data = await output_q.get()
        text=data['text']
        url=data['url']
        log_file = url.split('/')[-1]
        print("write",log_file,worker_id)
        open(log_file,'w').write(text)
        output_q.task_done()

async def main():
    input_q = asyncio.Queue()
    output_q = asyncio.Queue()

    url = "http://localhost:8000"
    url_files = []
    for i in range(1,11):
        url_files.append(f"{url}/apache_logs_{i:02d}.log")
    
    download_tasks = [asyncio.create_task(download(input_q,output_q,worker_id)) for worker_id in range(len(url_files))]
    writer_tasks = [asyncio.create_task(write_log(output_q,worker_id)) for worker_id in range(len(url_files))]

    for url in url_files:
        m = {"url":url}
        input_q.put_nowait(m)    

    await input_q.join()       
    await output_q.join()       

    for t in download_tasks:
        t.cancel()
    for t in writer_tasks:
        t.cancel()



if __name__ == '__main__':
    
    asyncio.run(main())