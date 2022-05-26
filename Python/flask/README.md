# Python / Flask 통한 웹서버 라고 부르기 애매한 무언가

* * *

### 5.15.41-gentoo-x86_64 를 사용해 Python 3.9.12 로 작성된 코드입니다.
###### Python 배운 첫날에 작성한 서버라 부족한 점이 있을 수 있어요.

* * *

### 폴더 구조
ROOT
- templates
   * gentoo.html
   * index.html
* README.md
* main.py

* * *

### 서버

* 플라스크를 사용해 라우팅 했습니다.<br/><br/>

* gentoo.html

```py
{% for i in range(1, 7) %}
   <h{{i}}>인스톨 젠투</h{{i}}>
{% endfor %}
{% for i in range(1, 7) %}
   <h{{7 - i}}>인스톨 젠투</h{{7 - i}}>
{% endfor %}
```
###### 사심을 담은 문법 <br/><br/>
