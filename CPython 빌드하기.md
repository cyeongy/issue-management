팀에서 사용 중인 파이썬 (3.8.0)을 리눅스 버전으로 포터블로 만들기 위해 CPython을 빌드했다.
해당 Ubuntu 22.04 LTS에서 configure && make && make install을 진행, Python 3.8.0 [GCC 11.3.0]이 완성되었다.

해당 포터블 파이썬을 Ubuntu 20.04 LTS 에서 실행했을 때 glibc6_2.32, 2.33, 2.34, 2.35 링크 에러가 났고 해당 에러의 경우 2가지 해결책이 존재했다.

- glibc 다운로드, configure --prefix=<사용자 디렉토리> && make && make install 
- GCC 다운그레이드

포터블 파이썬의 목적과, glibc의 빌드 시 크래시의 위험성 떄문에 Ubuntu 20.04 LTS에서 지원하는 glibc6_2.31, GCC 9.4.0으로 다운그레이드 후 재빌드로 해결하였다.
