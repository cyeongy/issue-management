(블로그)[https://velog.io/@cyeongy/Django-Model%EA%B3%BC-Form-1]

# Model과 Form

## Model과 Form의 형태

Django에서 DB Entity를 나타내기 위해서 django.db의 Model이라는 모듈을,
View 계층(장고에서는 View, 일반적으로는 Controller 계층)에 데이터를 안정적으로 전송하기 위해 Form이라는 모듈 제공한다.

이는 django 프로젝트를 생성했을 때 생기는 models.py 와 forms.py에 기본적으로 포함되어있다.

임의로 게시글 Post 모델을 작성한다면

- models.py
```py
from djang.db import models


class Post(models.Model):
	BOARD_CHOICE = (
    	('free', '자유 게시판'),
        ('game', '게임 게시판')
	)
	title = models.CharField('이름', 
    						max_length=20)
    body = models.TextField('내용')
    category = models.CharField('게시판', 
    							max_length=20, 
                                choices=BOARD_CHOICE, 
                                default='free')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_add=True)
    
```

- forms.py

```py
from django import forms
from .models import Post


class PostForm(forms.Form):
	title = forms.CharField(label='제목')
    body = forms.CharField(label='내용', widget=forms.Textarea)
    
class PostModelForm(forms.ModelForm):
	class Meta:
    	model = Post
        fields = ['title', 'body', 'cagetory']
        # 전부 입력받으려면 아래와 같이 사용
        # fields = '__all__'
	
```

---
## Null과 Blank의 차이

기본적으로 null=False, blank=False 상태이다.

### 필드 옵션의 기본적인 설명
1. null : **데이터베이스에 Null**값이 들어가는 것을 허용한다.
2. blank : Form(입력 양식)이 **공백** 상태로 받는 것을 허용. 
	form.is_valid()와 관계되어있다. 
    실제 데이터는 ''(공백)이 입력됨



```py
class Person(models.Model):
  name = models.CharField(max_length=255)  # 필수
  bio = models.TextField(max_length=500, blank=True)  # 선택 (null=True를 넣지 말자)
  birth_date = models.DateField(null=True, blank=True)  # 선택 (여기서는 null=True를 넣을 수 있다.)
```

### 주의사항

1. 문자열 필드에는 null=True를 사용하지 않는다.
TextField나 CharField같은 문자열 필드에는 null=True를 넣으면 안된다. 만약 아래와 같은 옵션을 주게된다면 문자열 데이터가 없을 때 Null 상태와 공백상태 2가지로 표현하게 된다.

```py
text = models.TextField(null=True, blank=True)
# null : 데이터가 없으면 Null 입력
# blank : 데이터가 없으면 공백('') 입력
```

2. BooleanField에 null옵션을 사용하려면 NullBooleanField를 사용한다.



> [10. null=True 와 blank=True 의 차이가 무엇인가요?](https://django-orm-cookbook-ko.readthedocs.io/en/latest/null_vs_blank.html)
[TIL.57 null=True 와 blank=True 의 차이(Django)](https://codermun-log.tistory.com/154)
[(번역) Django Tips #8 Blank or Null?](https://wayhome25.github.io/django/2017/09/23/django-blank-null/)
