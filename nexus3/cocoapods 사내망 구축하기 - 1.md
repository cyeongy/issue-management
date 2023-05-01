망분리가 이루어진 폐쇄망에서 코코아팟을 설치하려고 시도해보고 공부한 내용을 정리했습니다.
틀린 내용이 있을 수 있습니다.

# cocoapods 작동 원리 및 순서
#### 망분리 상태에서 podfile 작성 후 pod install을 한다면 cdn.cocoapods.org 접속 중 SSL 에러가 일어납니다.

해당 URL에서 podspec을 다운받을 수 없어 이 후 절차를 진행할 수 없는 것입니다.
장담은 못하지만 sudo gem install cocoapods 만 한 상태에서 인터넷을 끊는다면 동일한 상황이 발생할 것 같습니다.
개발팀에 직접 가서 팀원(세팅 초기에 보안팀에서 인터넷을 열어서 설치했습니다.)의 자리에서 디렉토리를 이것 저것 뜯어보고 조사해 본 결과 크게 2가지 차이점을 발견했습니다.

1. $HOME/Library/Cache/Cocoapods/* 
2. $HOME/.cocoapods/*


## podspec

1번의 경로는 코코아팟 패키지 소스가 저장되는 캐시 경로이고, 2번 경로는 PodSpec이 저장되는 캐시 경로입니다.
pod update가 실패하면 아래처럼 기존에 존재하던 소스 코드 라이브러리를 제거하고 다시 받는 것이고, pod install의 경우 podspec이 없어서 오류가 일어날 수 있고, 캐싱된 소스코드에 문제가 있을 수도 있습니다.

아래의 두 스크립트는 동일한 작동을 합니다.

```bash
pod cache clean --all
pod update
```


```bash
#!/usr/bin/env bash

rm -rf "${HOME}/Library/Caches/CocoaPods"
rm -rf "`pwd`/Pods/"
pod update
```

>https://gist.github.com/mbinna/4202236

코코아팟에서 pod install을 하는 이유는 개발을 편하게 하기 위해 다른 사람이 작성한 코드, 패키지를 다운받기 위함입니다. 아래 포스트를 읽으면서 큰 도움이 되어 일부 발췌하였습니다.

>
```rb
source 'https://github.com/CocoaPods/Specs.git' // (1)
source 'https://github.com/Artsy/Specs.git' // (2)
>
platform :ios, '9.0' // (3)
inhibit_all_warnings! // (4)
>
target 'MyApp' do
  pod 'GoogleAnalytics', '~> 3.1' // (5)
>
  # Has its own copy of OCMock
  # and has access to GoogleAnalytics via the app
  # that hosts the test target
>
  target 'MyAppTests' do
    inherit! :search_paths
    pod 'OCMock', '~> 2.0.1' // (6)
  end
end
>
post_install do |installer| // (7)
  installer.pods_project.targets.each do |target|
    puts target.name
  end
end
```
>(1) CocoaPods는 PodSpec을 통해서 라이브러리를 인식하고 분류합니다. 그러한 PodSpec이 있는 주소를 알아야 제대로 작동합니다. https://github.com/CocoaPods/Specs.git 는 따로 적지 않아도 기본값으로 세팅되어 있습니다.
>
>(2) 원하는 Specs 저장소를 연결 할 수 있습니다. 기업에서 사용할 때 private한 Specs 저장소로 사용하곤 했습니다.
>
>(3) platform :ios, '9.0' 해당 플랫폼, 버전에 맞춰서 설치합니다. 해당 라이브러리가 지원하는 경우에만 설치하게 됩니다.
>
>(4) inhibit_all_warnings! 를 써두면 빌드 시에 라이브러리에서 발생하는 warning을 무시합니다. 불필요한 warning이 너무 많으면 필요한 정보를 놓칠 수 있습니다.
>
 [CocoaPods 사용법과 파일구조](https://medium.com/@hongseongho/cocoapods-%EC%82%AC%EC%9A%A9%EB%B2%95%EA%B3%BC-%ED%8C%8C%EC%9D%BC%EA%B5%AC%EC%A1%B0-c0ea2ef362d6)

조금 첨언을 하자면 (1) 기본으로 세팅된 trunk repo의 경우 현재 cdn.cocoapods.org 를 통해 https://github.com/CocoaPods/Specs.git 의 내부 디렉토리에 존재하는 podspec.josn으로 리다이렉트 시켜줍니다. 

## cdn 탐색

>![](https://velog.velcdn.com/images/cyeongy/post/a9ad4bea-a786-4e0b-b49e-a9f304c9e96a/image.png)
https://github.com/CocoaPods/CocoaPods/blob/master/spec/fixtures/spec-repos/trunk
```
https://cdn.cocoapods.org/
```
https://github.com/CocoaPods/CocoaPods/blob/master/spec/fixtures/spec-repos/trunk/.url
>

>
```rb
module Pod
  class TrunkSource < CDNSource
    # On-disk master repo name
    TRUNK_REPO_NAME = 'trunk'.freeze
>
    # Remote CDN repo URL
    TRUNK_REPO_URL = 'https://cdn.cocoapods.org/'.freeze
>
    def url
      @url ||= TRUNK_REPO_URL
      super
    end
  end
end
```
> https://github.com/CocoaPods/Core/blob/master/lib/cocoapods-core/trunk_source.rb


cocoapods에서 기본적으로 source repo를 했을 때, 기본값으로 세팅된 repo의 위치를 표시하는 코드입니다. CDN에서 아래와 같은 순서로 podspec.json을 받아옵니다.

1. cdn.cocoapods.org/all_pods.txt 에서 pod의 이름을 조회하고

-> http://cdn.cocoapods.org/all_pods.txt

2. pod의 이름을 SHA(md5) 해싱 후 첫 3글자를 가져옵니다. 

ex) Toast-Swift -> **424**4FC178EA68ACF265646D58FD57B11

3. cdn.cocoapods.org/all_pods.txtall_pods_version\_?\_?\_?.txt 에서 버전을 조회합니다.

ex) https://cdn.cocoapods.org/all_pods_versions_4_2_4.txt

4. podfile에서 지정한 버전이 존재하면 podspec.json을 가져옵니다. 

ex) https://cdn.jsdelivr.net/cocoa/Specs/4/2/4/Toast-Swift/5.0.1/Toast-Swift.podspec.json

#### cdn.jsdeliver.net/cocoa는 코코아팟의 Spec.git의 cdn 주소입니다.

https://github.com/CocoaPods/Specs/blob/master/Specs/4/2/4/Toast-Swift/5.0.1/Toast-Swift.podspec.json 
https://cdn.jsdelivr.net/cocoa/Specs/4/2/4/Toast-Swift/5.0.1/Toast-Swift.podspec.json
