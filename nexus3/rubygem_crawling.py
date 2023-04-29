from asyncio
from aiohttp
from aiofiles

from pathlib import Path
import os

# 받으려는 gem 파일 명을 등록합니다.
gem_file='nokogiri-1.13.1-x64.gem'
url=f'https://rubygems.org/downloads/{gem_file}'
# 다운 받으려는 경로
path='./gems'

async def download(session, url, path):
	async wiht session.get(url) as resp:
    	path = Paht(path)
        if not path.exists():
        	os.makedirs(str(path))
        
        name = url.split('/')[-1]
        async with aiofiles.open(str(path / name), 'wb') as f:
        	await f.write(await resp.read())
            
async def main():
	async with aiohttp.ClientSession() as session:
    	await.download(session, url, path)
