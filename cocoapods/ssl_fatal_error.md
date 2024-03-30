
# SSL 인증 에러

이전에 SSL 인증 에러로 인해 pod install을 할 수 없다고 이야기 했었던 자료를 읽어보았다.

문득 생각나는 키워드로 다시 검색을 해보니 내가 겪었던 상황과 비슷한 케이스를 스택오버플로에서 찾을 수 있었다.

(https://stackoverflow.com/questions/20939105/pod-install-returns-fatal-error-ssl-certificate-issue)

fatal: unable to access 'https://github.com/CocoaPods/Specs.git/': SSL certificate problem: Invalid certificate chain

``` bash
GIT_SSL_NO_VERIFY=true pod install
```

도중에 위와 같은 스크립트로 SSL 인증 없이 깃에 접속하면 될 수도 있겠다는 생각이 들었다.
물론 폐쇄망 환경에서 다시 동일한 업무를 진행하지 않는다면 정답이 나올 것 같지는 않다.
