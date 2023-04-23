## 도커 시작하기

### 이미지 찾기 및 설치
```bash
# docker hub에 있는 이미지를 찾는 명령어
docker search image

# docker hub에 있는 이미지를 설치하는 명렁어
docker pull [library/]image[:tag]

# 도커 이미지를 생성하는 명령어
# 설치한 이미지의 이름을 지정하려면 --name "원하는 이름" 으로 지정할 수 있다
# 이름을 설정하지 않으면 임의로 naughty_khayyam같은 치기 어려운 이름으로 생성해주니 꼭 지정해주자...
docker create --name name image[:tag]

# local repository에 설치된 도커 이미지를 확인하는 명렁어
docker ps [-a|--all]

# 설치한 이미지를 시작하는 명령어
# container는 --name으로 지정할 수도 있다
docker start [OPTION] container

# docker run 설명
# Local repository에 이미지가 있다면 create + start
# 이미지가 없다면 pull + create start 로 작동한다
docker run [OPTIONS] image

# my-nginx라는 이름의 nginx 컨테이너를 만든다
docker run --name my-nginx nginx
```



### 도커 네이밍 규칙: [이미지 저장소 이름]/[이미지 이름]:[이미지 태그]

>
rule 1. 도커의 공식 이미지 태그는 dockerhub의 library 저장소에 존재한다.
rule 2. 이미지 태그(버전)을 명시 하지 않으면 최신 버전(latest)가 지정된다.
rule 3. 저장소 이름은 생략할 수 있고, 생략 시 암묵적으로 library를 지정한다.

docker pull image 명령어는
docker pull library/image:latest 가 적용된다.

### 도커 이미지 이름 변경

```bash
docker image tag [원본 저장소]/[원본 이미지]:[원본 태그] [커스텀 저장소]/[커스텀 이름]:[커스텀 태그]
```
---
## 도커 이미지 만들기
### 도커 이미지를 만드는 2가지 방법
1. Docker Container를 바탕으로 만들기 (Snapshot)
2. Dockerfile을 통해 Source Code를 바탕으로 Image 생성



### 컨테이너의 주요 용어
- chroots : 프로세스의 루트 디렉토리 변경
- namespace : 커널 자원들을 구분해서 프로세스 테이블(PIDs), ipc, 네트워크(IP adress, 방화벽), User ID, 마운트 포인트 등을 가상화
- Cgroups : 프로세스의 리소스를 격리하고 사용을 제어


