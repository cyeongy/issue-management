parallel 문법의 팁은 stage와 stages는 번갈아가면서 나와야한다.
절대 stage 안에 stage가 바로 나올 수 없고, stages 안에 stages가 나올 수 없다.


## 간단한 병렬 빌드
First Stage : 소스 코드 클론
Second Stage : 분할 후 병렬 빌드
Third Stage : upload
![](https://velog.velcdn.com/images/cyeongy/post/36b16de8-cec1-4cd1-905a-3d030e7e1321/image.png)


```java
pipeline {
    agent any

    stages {
        stage('First Stage'){
            steps{
                echo "First Stage"
            }
        }
        stage('Second Stage') {
            parallel {
                stage('parallel 1st'){
                    steps{
                        echo 'p1'
                    }
                }

                stage('parallel 2st'){
                    steps{
                        echo 'p2'
                    }
                }

                stage('parallel 3rd'){
                    steps{
                        echo 'p3'
                    }
                }
            }
        }
        stage('Third Stage'){
            steps{
                echo 'Third Stage'
            }
        }
    }
}
```


## 의존성이 있는 병렬 작업

parallel1과 paralle2와 의존성이 존재할 때 아래와 같이 빌드한다
ex) 데이터 백업 혹은 동기화
![](https://velog.velcdn.com/images/cyeongy/post/eb9b1d58-daca-4102-aab6-98ddbe6bfdb5/image.png)

```java
pipeline {
    agent any

    stages {
        stage('First Stage'){
            steps{
                echo "First Stage"
            }
        }
        stage('parallel1'){
            parallel {
                stage('parallel1 1st'){
                    steps{
                        echo 'p11'
                    }
                }

                stage('parallel1 2st'){
                    steps{
                        echo 'p12'
                    }
                }

                stage('parallel1 3rd'){
                    steps{
                        echo 'p13'
                    }
                }
            }
        }
        stage('parallel2') {
            parallel {
                stage('parallel2 1st'){
                    steps{
                        echo 'p21'
                    }
                }

                stage('parallel2 2st'){
                    steps{
                        echo 'p22'
                    }
                }

                stage('parallel2 3rd'){
                    steps{
                        echo 'p23'
                    }
                }
            }
        }
        
        stage('Third Stage'){
            steps{
                echo 'Third Stage'
            }
        }
    }
}
```

## 순서는 존재하나 의존성은 없는 병렬 작업, 빌드

파이프라인끼리 의존성은 없지만 JOB의 순서가 있는 경우, 매우 일반적인 상황
ex) iOS, Android 앱을 동시에 빌드할 때 

![](https://velog.velcdn.com/images/cyeongy/post/ea777f4e-c793-4305-85cd-a48c10d862b6/image.png)
```java
pipeline {
    agent any

    stages {
        stage('First Stage'){
            steps{
                echo "First Stage"
            }
        }
        stage('Second Stage'){
            parallel {
                stage('parallel1'){
                    stages {
                        stage('parallel1 1st'){
                            steps{
                                echo 'p11'
                            }
                        }

                        stage('parallel1 2st'){
                            steps{
                                echo 'p12'
                            }
                        }

                        stage('parallel1 3rd'){
                            steps{
                                echo 'p13'
                            }
                        }
                    }
                }
            
                stage('parallel2') {
                    stages {
                        stage('parallel2 1st'){
                            steps{
                                echo 'p21'
                            }
                        }

                        stage('parallel2 2st'){
                            steps{
                                echo 'p22'
                            }
                        }

                        stage('parallel2 3rd'){
                            steps{
                                echo 'p23'
                            }
                        }
                    }
                }
            }
        }
        
        stage('Third Stage'){
            steps{
                echo 'Third Stage'
            }
        }
    }
}

```
