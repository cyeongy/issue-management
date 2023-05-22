# ModuleNotFound: SSL Error

## 에러 로그

```bash
ModuleNotFoundError: No module named '_ssl'
```

파이썬 버전관리를 위해 CPython을 빌드해서 만든 포터블 파이썬에서 웹서버를 띄우기 위해 uvicorn을 실행 했을 때 \_ssl을 찾지 못하는 에러가 발생했습니다.

## 원인

인터넷에서 다양한 블로그와 스택오버플로우의 글을 읽은 결과 내린 결론은 Python에서 openssl은 기본 모듈에 속하지만, 임베디드 파이썬에서는 직접 빌드 패키지를 추가해주어야 한다는 사실이었습니다.

## 해결책

```bash
sudo apt install libssl-dev openssl

./configure --with-ssl-default-suites=python && make all && make install
```

우분투 기준으로 libssl-dev와 openssl 패키지를 설치한 후 아래와 같은 구문으로 새로 빌드를 진행합니다.

기존에 빌드된 버전이 있다면 pip freeze를 통해 개발 환경을 보존해두고 파이썬을 새로 빌드하면 되겠습니다.
