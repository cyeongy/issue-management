윈도우에서 JAVA_PATH가 C:\Program Files\Java\[JDK 버전]
OSX(맥)에서 JAVA_PATH는 /Library/Java/JavaVirtualMachines/[JDK 버전]/Contents/Home

이렇게 지정된다.

```bash
# JDK의 설치 경로와 버전을 확인하는 명력어 (대문자)
/usr/libexec/java_home -V

# JDK의 경로를 반환하는 명령어 (소문자)
# 숫자를 지정하지 않으면 가장 최상단, 최신버전이 지정된다.
# 1.8.0과 11.0이 있을 떄 1을 넣으면 11버전이 1. 을 넣으면 1.8.0 버전이 지정된다.
# 2를 넣으면 11.0 버전이 지정됨
/usr/libexec/java_home -v [숫자]

# java는 /usr/bin/java를 호출한다.
java
/usr/bin/java
```

맥에서 자바 PATH를 넣을 때 대부분 JDK를 고정하고 JDK 경로 확인 후 아래와 같은 방식으로 작성하곤 하는데
```bash
PATH=/Library/Java/JavaVirtualMachines/[JDK 버전]/Contents/Home/bin:$PATH
```
아래처럼 $()을 사용하여 command 호출을 사용하면 편하게 JAVA PATH를 .zshrc 혹은 .bashrc에서 바인딩 할 수 있다.
```bash
JAVA_HOME=$(/usr/libexec/java_home -v 11)
PATH=$JAVA_HOME/bin:$PATH
```

폐쇄망, 사내망에서 OpenJDK를 tar.gz로 설치하려면 마찬가지로 아래처럼 설치한다.
혹은 
```bash
# tar
tar -xvf openjdk-11.0.2.tar /Library/Java/JavaVirtualMachines

# tar.gz
tar -zxvf openjdk-11.0.2.tar /Library/Java/JavaVirtualMachines
```

혹은 특정 유저만 사용할 수 있게 설치한다면 /Users/{맥 유저이름}/Library/Java/JavaVirtualMachines 에 설치해도 무방하다.

brew install을 하면 해당 경로로 설치될 것이다.

