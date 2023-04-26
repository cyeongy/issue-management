# Nexus3 Repository 사내망 구축하기

## PIP 환경설정

Nexus3 설치와 라우팅 룰 설정을 끝내고 

빌드 머신(윈도우, 리눅스, 맥OS) -> Nexus3 -> 프록시 -> 외부 저장소

를 순서로 설치하게되면서

각각 윈도우, 리눅스, 맥OS의 pip가 넥서스를 바라보게 만들었다.



pip.ini 혹은 pip.conf 파일의 위치와 존재는 아래 명령어로 확인할 수 있다.

```bash
# 윈도우
pip config debug

# 맥, 리눅스
pip3 config debug
```
----
|OS|Global|Local|
|---|---|---|
|Window 10|C:\ProgramData\pip\pip.ini|%APPDATA%\pip\pip.ini|
|맥, OSX|/Library/Application Support/pip/pip.conf|$HOME//Library/Application Support/pip/pip.conf
|Linux|/etc/pip.conf|$HOME/.config/pip/pip.conf

- 가상환경 경로
	$VIRTUAL_ENV/pip.conf (리눅스, 맥), $VIRTUAL_ENV/pip.ini (윈도우)


나는 아래와 넥서스만 바라보게 할 것이라 아래와 같이 작성했다

```
[global]
index-url={Nexus3 Repsitory URL}:{PORT}/repository/{파이썬 repo}/simple
trusted-host={Nexus3 Repsitory hostname}
```


Gem의 경우 아래와 같은 명령어로 편집할 수 있다.


```bash
gem sources --add http://localhost:8081/repository/{루비젬 repo}/groups/gems-all/

gem sources --remove https://rubygems.org/

gem sources -c
```





>https://pip.pypa.io/en/stable/topics/configuration/
>
>https://help.sonatype.com/repomanager2/ruby%2C-rubygems-and-gem-repositories
