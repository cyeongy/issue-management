---
description: AMI 에서 파이썬을 다운로드 하는 방법
---

# Amazon-linux2

## Amazon Linux 와 CentOS

Amazon Machie Image, 아마존 리눅스 이미지는 레드햇 베이스 이미지입니다.

레드햇 계열의 배포판, CentOS를 사용해본 분이라면 굉장히 익숙하게 사용할 수 있을 것이라 생각합니.\
차이점으로는 레드햇과 아마존에서 관리하는 yum 패키지가 다릅니다.

예를 들자면 NFS(network file system)을 캐싱하는 cachefilesd 패키지의 경우 CentOS에서는 검색 가능하나, Amazon Linux에서는 별도의 컴파일, 빌드가 필요합니다.

### amazon-linux-extras

앞서 아마존에서 관리하는 yum 패키지가 다르다고 말씀 드렸는데, AMI에서 extras 라이브러리에서 소프트웨어 패키지를 설치할 수 있습니다.

#### Extras 패키지 확인

```bash
$ which amazon-linux-extras
/usr/bin/amazon-linux-extras
```

만약 AMI 이미지로 인스턴스를 시작하였음에도 사용할 수 없다면 yum으로 설치해줍시다.

```bash
$ sudo yum install -y amazon-linux-extras
```

#### Python 버전(3.8) 확인 및 활성화

```bash
$ amazon-linux-extras | grep python
44  python3.8                availabl    [ =stable ]
```

```shell
$ sudo amazon-linux-extras enable python3.8
44  python3.8=latest         enabled     [ =stable ]
```

#### yum 패키지 설치

```bash
$ sudo yum install python3.8
```

```bash
$ which python3.8
/usr/bin/python3.8
```

## Extras 패키지 설치와  CPython 빌드 차이

회사에서 필요에 의해 파이썬 3.8.0에 맞추어 CPython을 빌드하고, 관리해보면서 Extras 패키지  설치와의 차이점이 몇가지 있는 것 같다.&#x20;

#### 설치 경로&#x20;

* Extras 패키지 : /usr/bin/python
* CPython 빌드 : /usr/local/bin/python

물론 CPython을 빌드 할 때, configure --prefix=/usr 을 통해 AMI와 동일하게 설정할 수 있지만, 팀에서 파이썬을 메인 스크립트 언어로 채택하고, 포터블 파이썬을 빌드하게 되면서 우선적으로 느낀 것은 경로의 차이였다.

#### GCC

AMI는 레드햇 베이스의 이미지이고, CPython을 빌드한 환경은 Ubuntu22.04, 사용환경은 20.04 이기에 데비안과 레드햇의 차이가 있을 지 몰라도 GCC의 버전 차이가 존재하였다.

|             | Ubuntu 20.04 | Ubuntu 22.04 | Amazon Linux (Red Hat)     |
| ----------- | ------------ | ------------ | -------------------------- |
| 기본(default) | GCC 9.4.0    | GCC 11.2.0   | GCC 7.3.1 (extras package) |
| CPython 빌드  | GCC 9.4.0    | GCC 11.3.0   |                            |
