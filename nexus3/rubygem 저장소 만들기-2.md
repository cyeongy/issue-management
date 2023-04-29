지난 포스팅에서 gem install로 개인 저장소를 만들었다면 캐시에 저장된 .gem 파일을 불러 오는 방법이다.


```
# Ruby 버전에 따라 다릅니다
# Window는 Ruby installer에서 제공하는 최신 버전인 3.2.2-1(x64) 기준입니다
C:\Ruby32-x64\lib\ruby\gems\3.2.0\cache/

# Mac
# Users의 홈 디렉토리에서 찾을 수 있습니다
$HOME/.gem/ruby/3.2.0/cache/
```

## 플랫폼 의존성이 존재하는 경우
사내망에서 사용하는 개발환경과 비슷하게 맞춘 상태에서 gem install을 통해 캐싱을 해오면 좋겠지만 윈도우나 맥에서 인스톨을 하면 몇 종류의 패키지는 의존성이 존재하여 동일한 세팅에서 다운로드 해야하는 경우가 있습니다. 

```bash
패키지이름-버전[-java|-x86|-x64|-mingw32|-mingw|-x86_64|-darwin].gem
```

그럴 때, rubygems.org/downloads/{gem 파일 이름} 에서 크롤링하면 편하게 다운받을 수 있습니다.
모든 파일의 의존성을 알고 있는 것은 아니지만 nokogiri나 ffi과 같은 특정 패키지들은 
>
- Linux:
x86-linux and x86_64-linux (req: glibc >= 2.17)
aarch64-linux and arm-linux (req: glibc >= 2.29)
- Darwin/MacOS: x86_64-darwin and arm64-darwin
- Windows: x86-mingw32, x64-mingw32, and x64-mingw-ucrt
- Java
>
https://rubygems.org/downloads/nokogiri-1.13.1-x86_64-darwin.gem
https://rubygems.org/downloads/nokogiri-1.13.1-x86_64-linux.gem
https://rubygems.org/downloads/nokogiri-1.13.1-x86-linux.gem


```py
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

```
