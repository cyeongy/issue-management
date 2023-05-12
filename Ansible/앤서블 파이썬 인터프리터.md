# 앤서블 변수

## 기본 매개 변수 표
|이름|기본값|설명|
|---|---|---|
|ansible_host|호스트 이름|SSH로 연결하려는 호스트 명, IP|
|ansible_port|22|SSH 포트|
|ansible_user|root|SSH 연결 사용자|
|ansible_password||SSH 비밀번호|
|ansible_connection|smart(자동)|앤서블이 다른 호스트에게 연결하는 방법|
|ansible_private_key_file| |SSH 개인 키 위치|
|ansible_shell_type|sh|SSH 쉘 타입|
|ansible_python_interpreter|/usr/bin/python| 파이썬 인터프리터 위치|
|ansible_*_ineterpreter||다른인터프리터 위치|

## 파이썬 인터프리터

앤서블은 Host에서 작성한 playbook을 가공하여 SSH로 원격 노드에 연결하여 스크립트를 실행합니다. 
Linux의 경우 지정한 위치에 파이썬 인터프리터가 없다면 아래 순서대로 파이썬 바이너리를 탐색합니다.

python3.10, python3.9, python3.8, python3.7. python3.6, python3.5, /usr/bin/python3, /usr/libexec/platform-python, python3.7, /usr/bin/python, python


