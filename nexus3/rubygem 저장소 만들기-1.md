# rubygem 저장소 만들기-1



## rubygem 저장소 만들기-1

지난 포스팅에서 Nexus3와 pypi 저장소와 연결을 했는데, 오늘은 rubygem과 연결을 하겠습니다.

### .gem 캐싱하기

### 원격 저장소 등록

우선 사내저장소를 만들기 전에 인터넷 망에서 캐싱을 위해 mirror 저장소를 만듭니다.

![](https://velog.velcdn.com/images/cyeongy/post/95a8eaf4-f7f0-480b-a8a6-e066ca664783/image.png)

지금은 집에서 테스트 중이므로 사내망을 대신할 hosted 타입의 로컬 저장소도 만들었습니다.

![](https://velog.velcdn.com/images/cyeongy/post/de71d60b-4ccd-4142-aa4e-6f5098123aba/image.png)

### rubygems install 경로 지정

아래 명령어를 실행해서 삭제합니다. swift 패키지 관리에 자주 사용되는 cocoapods을 설치하기 위해 맥에서 접속했습니다.

```bash
# 넥서스 리포지토리 등록 (remote repository를 통해서 다운로드)
gem sources --add http://localhost:8081/repository/{루비젬 repo}/

# 루비젬 저장소 삭제
gem sources --remove https://rubygems.org/

# cache 삭제
gem sources -c
```

![](https://velog.velcdn.com/images/cyeongy/post/24e41757-041c-4ca9-a4c1-d53e3b0a6ce6/image.png)

cocoapods를 설치하다보니 root 경로에 쓰기 권한이 없다고 거부가 되었다. sudo권한으로 다시 설치를 진행하자

![](https://velog.velcdn.com/images/cyeongy/post/b517fb73-e219-4abc-81c5-d553d237bacc/image.png)

맥에서 ruby를 업그레이드 하지 않았다면 기본으로 설치된 2.6.10버전이라 activesupport 7.0.4.3에서 6.1.7.3으로 버전을 낮춰서 설치하라고 경고가 나올텐데 무시하고 넘어가도 좋다. 사실 Install 보단 Fetching을 끝마쳐서 캐시 서버에 gem파일을 저장하는 것이 더 중요하다.

### 리포지토리 확인

리포지토리를 확인하면 아래처럼 .gem 파일과 .gemspec.rz 파일이 생긴다. nexus3을 크롤링해서 .gem 파일을 다운로드 후 사내망에 다시 업로드하면 해결 할 수 있다.

![](https://velog.velcdn.com/images/cyeongy/post/08ed536a-c415-4e95-8984-6dfa7c707567/image.png)
