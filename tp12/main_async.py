#!/usr/bin/env python
import sys
import os
import asyncio


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    # print('Hello ...')
    # await asyncio.sleep(5)
    # print('... World!')

    c = await add(5,6)
    print("c",c)


    r = await asyncio.gather(add(5,6),add(6,7),add(51,16),add(5,56))
    print(r)

if __name__ == '__main__':
    asyncio.run(main())
