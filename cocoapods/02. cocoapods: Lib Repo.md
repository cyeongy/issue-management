# Library

지난 Spec Repo에서 podspec을 저장했다면, Lib Repo는 말 그대로 소스 코드가 저장된 리포지토리를 의미합니다.
개발자 입장에서 Podfile 최상단에 source '<POD REPO URL\>'만 작성하는 것이 최고의 편의성이 아닐까 생각합니다.

물론 REPO 관리를 위해 분리할 수도 있지만 굳이 분리해야하는 이유에 대해서는 아직 체감하지 못했습니다.

다만 저같은 경우, 회사에서 개인에게 할당된 gitlab private repo가 5개였기 때문에 github에서 branch와 tag를 보존하기 위해 Public Pod URL에서 git clone을 통해 가져온 파일들을 git remote add를 통해 gitlab에 추가하려 했지만 개수 제한으로 구조를 조금 변경하였습니다.

## Repo 하나에 몰아서 저장하기


- 원래 계획

pod lib 마다 사내 gitlab에 저장소를 만들어서 git clone으로 .git 파일 (branch, tag 정보)를 보존
git remote add를 통해 podspecd의 source 정보만 수정

```
├── Toast-Swift/
│   ├── Source/
│   │   └── **/
│   │       └── *.swift
│   └── Test/
│       └── **/
│           └── *.swift
└── RxSwift/
    ├── Platform/
    │   └── **/
    │       └── *.swift
    ├── RxSwift/
    │   ├── **/
    │   │   └── *.swift
    │   └── exclude/
    │       └── *.swift
    ├── RxCocoa/
    │   ├── **/
    │   │   └── *.swift
    │   └── exclude/
    │       └── *.swift
    └── RxRelay/
        ├── **/
        │   └── *.swift
        └── exclude/
            └── *.swift
```

- 수정안

podspec의 tag 정보를 제외하고 최상위 디렉토리에서 서브 디렉토리로 관리
(서브 모듈은 결과적으로 git 리포지토리가 있어야해서 제외)

```
# https://gitlab.com/cyeongy/CommonLib.git  이라고 가정합니다.
└── CommonLib/
    ├── Toast-Swift/
    │   ├── Source/
    │   │   └── **/
    │   │       └── *.swift
    │   └── Test/
    │       └── **/
    │           └── *.swift
    └── RxSwift/
        ├── Platform/
        │   └── **/
        │       └── *.swift
        ├── RxSwift/
        │   ├── **/
        │   │   └── *.swift
        │   └── exclude/
        │       └── *.swift
        ├── RxCocoa/
        │   ├── **/
        │   │   └── *.swift
        │   └── exclude/
        │       └── *.swift
        └── RxRelay/
            ├── **/
            │   └── *.swift
            └── exclude/
                └── *.swift          
```

	RxSwift에서는 내부 디렉토리로 RxSwift와 RxCocoa, RxRelay를 관리하고 각각의 podspec이 존재합니다.	
    
### podspec 변화

해당 서비스의 원본 git repo name이 최상단 디렉토리로 들어가게됩니다.

- 원본 podspec

```rb
  s.source           = { :git => "https://github.com/ReactiveX/RxSwift.git", :tag => s.version.to_s }

  s.header_dir            = "RxCocoa"
  s.source_files          = 'RxCocoa/**/*.{swift,h,m}', 'Platform/**/*.swift'
  s.exclude_files         = 'RxCocoa/Platform/**/*.swift', 'Platform/AtomicInt.swift'
```

- 수정 podspec

```rb
  s.source           = { :git => "https://gitlab.com/cyeongy/CommonLib.git" }

  s.header_dir            = "RxCocoa"
  s.source_files          = 'RxSwift/RxCocoa/**/*.{swift,h,m}', 'RxSwift/Platform/**/*.swift'
  s.exclude_files         = 'RxSwift/RxCocoa/Platform/**/*.swift', 'RxSwift/Platform/AtomicInt.swift'
```

