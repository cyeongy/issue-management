# 앤서블 (Ansible)

앤서블은 RedHat에서 공개, 관리하는 오픈 소스 프로비저닝 툴입니다.

프로비저닝이란 "IT 인프라를 생성하고 설정하는 프로세스로, 다양한 리소스에 대한 사용자 및 시스템 액세스를 관리하기 위해 필요한 단계" 입니다.

간단히 말해서 OS만 설치된 컴퓨터를 빌드/배포 머신이나 서버로 구축하기 위한 필수적인 초기 단계입니다.

예를 들어, java 기반의 웹 서비스를 배포하기 위해서는 jdk를 설치하거나, 빌드 머신에는 CM 툴인 git, svn, perforce 등의 프로그램등을 설치하는 과정을 프로비저닝이라 부르고, 앤서블은 그 과정을 관리하는 툴입니다.

앤서블은 기본적으로 SSH와 yaml을 통해 작업을 관리하나, 윈도우의 경우 앤서블 1.7 이상에서 WinRM (5895, 5986)을 사용하여 제어하는 기능을 추가하였습니다.

OpenSSH 의 경우 해당 문서에서 언급하지 않습니다.

# 설치 사양 및 준비

## 제어 노드 (Control Node, Master)

- Linux, Unix
  - Python2 (>= 2.7) or Python3 (>= 3.5)
- Windows
  - Windows에서 앤서블을 설치하여 다른 OS를 관리하는 기능은 제공하지 않습니다
  - WSL(Window Subsystem for Linux)를 사용하여 Ansible을 설치할 수 있습니다.

## 관리 노드

- Linux, Unix
  - Python2 (>= 2.7) or Python3 (>= 3.5)
  - SSH (기본 22포트)
- Windows
  - Powershell (>= 3.0) & .Net Framework (>= 4.0)
    (파워쉘 3.0 버전에는 메모리 핫픽스가 필요합니다. 4.0 이상을 추천합니다.)
  - WinRM (5985, 5986 포트)
  - Windows 2008 SP1 이상
  - WinRM 활성화
  - WinRM Auth/Basic = True 활성화


### WinRM 활성화

```powershell
# WinRM 활성화
winrm quickconfig

# WinRM Auth 상태 체크
winrm get winrm/config/client/Auth

# WinRM Auth/Basic 활성화
winrm set winrm/config/service/auth @{Basic="true"}

# winrm 설정 확인
winrm get winrm/config

# Listener 포트 확인
winrm e winrm/config/listener

```


# Ansible 설치

```bash
pip3 install ansible
python3 -m pip install ansible
```

apt, yum 등의 여러 인스톨이 가능하나 git에서 개발 리소스로 직접 받아오는 pip로 인스톨 하였습니다.

추후 ansible 모듈을 직접 개발하는 가능성도 열어 두기 위함입니다.

# Ansible 연결

## SSH

### 패키지 설치
앤서블 연결을 위해 필요한 패키지를 설치해야합니다.
```
sudo apt install sshpass
```

### SSH Key 등록하기 (비밀번호 미사용)

- ssh-keygen
- ssh-copy-id

```bash
# ssh 키 생성하기
ssh-keygen -t rsa

# ssh 공개키 복사하기 (to remote host)
ssh-copy-id username@hostname

# 예시
ssh-copy-id ubuntu@10.92.114.67
```

### Known Host 등록하기 (비밀번호 사용)

- ssh-keyscan
- 옵션
  - -H : 호스트 이름 해싱
  - -t : 암호화 타입 지정 (rsa, ecdsa, ... 기본값은 대표적인 암호화 4개)
  - -f : 파일로 지정
  - -v : verbose
  - -p : port
  - -4 : IPv4만 등록
  - -6 : IPv6만 등록

```bash
ssh-keyscan -t rsa [-f 호스트파일] 10.92.114.67 >> ~/.ssh/known_hosts

# 호스트파일 예시
192.168.11.0/24
10.92.114.67
aws.devops.com
10.92.181.26, 10.92.181.27, 10.36.29.21, 10.36.48.12
```
> SSH 접속이나 ssh-copy-id 를 통해 등록하는 경우 (yes/no/[fingerprint]) 를 입력하는 과정이 Knwon hosts 등록 과정입니다. 
> 
> known host를 등록하는 ssh-keyscan은 Jenkins via SSH 에서 known host policy 에서 요긴하게 사용할 수 있습니다.
> 
> 앤서블에서 Knonw hosts 옵션을 무시하는 방법도 있으나 추천하지 않습니다.
> 
> 방법은 아래와 같습니다
> 1. 환경변수 등록
> ```bash
> export ANSIBLE_HOST_KEY_CHECKING=False
> ```
> 2. ansible.cfg 편집
> ```ansible.cfg
> [default]
> hosts_key_checking = False
> ```


## WinRM

### pywinrm 설치

앤서블에서 윈도우를 관리하려면 winrm으로 제어하며, pywinrm 패키지를 설치해야합니다.

위에서 앤서블을 pip로 인스톨한 이유도 어찌보면 어차피 pywinrm도 pip로 설치해야 하는 것, 앤서블도 pip로 설치한 점도 없지않습니다.

```bash
pip3 install pywinrm
python3 -m pip install pywinrm
```

* window AD 계정에서 basic 로그인이 안되는 경험이 있습니다. 가급적이면 로컬 계정으로 진행합시다.
