- 배경지식 : https://velog.io/@yuru/%EA%B0%9C%EB%B0%9C-%EB%B0%B0%EA%B2%BD%EC%A7%80%EC%8B%9D%EC%A0%95%EB%A6%ACfeat.IT-%EA%B0%9C%EB%B0%9C%EC%9E%90%EC%99%80-%EC%9D%BC%ED%95%A0-%EB%95%8C-%ED%95%84%EC%9A%94%ED%95%9C-%EB%AA%A8%EB%93%A0-%EA%B0%9C%EB%B0%9C%EC%A7%80%EC%8B%9D

---
# ** eXERD를 이용한 모델링

## 1. 모델링 결과를 테이블로 변환
- 사전 준비 사항
  - 접속할 데이터베이스
  - 데이터베이스 드라이버

### 1) 데이터베이스 연결
- [Window] >> [Show View] >> [eXERD] >> [Model]
- 오라클은 스키마 이름을 접속 계정 이름으로 변경
- MySQL은 스키마 이름을  DB 이름으로 변경

### 2) eXERD 메뉴에서 포워드 엔지니어링 수행

## 2. 이미 만들어진 테이블로부터 E-R 다이어그램 추출
- Reverse Engineering : 구현된 코드로부터 설계정보를 만드는 것

## 오류 해결방법
- MySQL 8.x 이상 버전에서 timezone 오류 시,
- 키 serverTimezone, 값 UTC으로 설정

## ReadMe 작성 규칙
- 개발 환경
- 모델의 구조 설명
	- .summary()


---
# ** Web Programming
- 클라이언트가 HTTP/HTTPS 프로토콜을 이용해서 서비스를 받을 수 있도록 한 프로그래밍

## 1. 웹서버에 요청하는 방법
- 웹 브라우저를 이용한 요청
- 클라이언트용 프로그램을 제작하여 요청
- 예시
	- 리눅스 : ```wget```

## 2. 요청을 하기 위한 url 구조
- 프로토콜://[호스트, 도메인이나 ip주소][:port번호][요청]?[파라미터]
- [port번호]가 생략 가능한 경우 : 프로토콜의 기본포트를 사용하는 경우
	- HTTP:80, HTTPS:443
	- HTTP(Hypertext Transfer Protocol)
- [요청] 경로가 생략되는 경우 : 이 경우는 서버에서 처리하는 문장이 있는 경우
- [파라미터] : 이름=값. 파라미터는 클라이언트가 웹 서버에 전달하는 데이터.
	- 검색시 클라이언트가 웹 서버에 전달하는 파라미터는 검색어에 해당함
- Fragment : 마지막에 #이 붙음
	- 문서 내의 특정 위치로 이동할 때 사용함. 생략되는 경우가 대부분.

## 3. 웹 프로그래밍의 결과
### 1) 정적인 페이지
- 요청이 오면 항상 동일한 내용을 출력함
- 이 경우 별도의 서버 처리 코드가 필요 없음
- html, CSS, JavaScript로만 구성

### 2) 동적인 페이지
- 서버가 요청을 처리하여 동적으로 출력함
- Java, Python등 서버 사이드 프로그래밍 언어로 별도의 서버 프로그램을 작성해야 함

## 4. 동적인 페이지 만드는 방법(2가지)
### 1) CGI
- CGI (Common Gateway Interface)
- 클라이언트 요청을 하나의 프로세스로 처리하는 방식
- 언어 : Perl의 방식
### 2) 애플리케이션 서버 방식
- 클라이언트 요청을 하나의 스레드로 처리하는 방식
- 동시에 여러 클라이언트 요청 처리가 가능함
- 언어 : Java(Java Server Page), Python, C#(ASP.NET), PHP, Ruby 등
- 우리나라
	- Java 주로 이용함. 간단한 웹사이트는 PHP, Node에서 많이 작성
	- Java는 Spring 프레임워크가 있어서 규모가 큰 사이트 작성 수월함

## 5. 웹 프로그래밍의 구조
```
[사용자 애플리케이션] <==> [Web Server] <==> [Application Server] <==> [Repository]
```
- 장고/플라스크는 웹서버의 역할을 할 수 없음
- FrontEnd : 사용자 애플리케이션 만드는 것
- BackEnd/ServerSideProgramming : Application Server를 만듦

- 웹브라우저에서 사용자 애플리케이션을 작동하기 위해 html, CSS, JavaScript 이용함
- html : 웹 브라우저에 출력할 문서 구조를 만드는 언어
- CSS : html에 디자인 입히는 언어
	- 최근에는 이 문법을 이용해서 GUI 프로그래밍 디자인도 설정함
- JavaScript : html의 동적 기능을 부여하기 위한 언어
	- 최근에는 여러 라이브러리를 개발하여 다양한 용도로 사용됨

## 6. Python 웹 프레임워크
### Full Stack Framework
	- 클라이언트와 서버를 전부 개발하는 것
- MEA(R)N
	- MongoDB : 저장소
	- Express.js : 서버
	- Angular.js(React.js) : 클라이언트
	- Node.js : 애플리케이션 서버
- 클라이언트 / 서버를 모두 JavaScript로 구현

### 1) Django
- Full Stack Framework
- 하나의 프로젝트에 여러 개의 Application 생성 가능함
- 자체 ORM 기능 제공
	- ORM(Objective Relation Mapping)
	- DB 연동 할 때
	- 하나의 클래스와 테이블을 매핑하고, 클래스의 인스턴스로 DB 작업 수행하는 것
	- SQL이 필요 없음
		- SQL을 직접 이용하는 경우, DB마다 SQL문이 약간씬 다르기 때문에
		- 특정 DB를 연동하는 코드를 작성한 상태에서 DB를 변경하면 코드도 수정해야 함
	- ORM을 쓰는 경우 DB연동 부분 코드만 수정하여 DB를 바꿔 쓸 수 있음
- 기본적인 틀을 제공함

### 2) Flask
- Micro Framework
- 하나의 프로젝트에 하나의 Application 생성 가능함
- 별도의 ORM이 없음
- 기본적인 틀이 없음 - 확장이 용이함
- Flask 사용 기업 : Naver, Linked In


# ** Flask
## 1. 특징
- Python 기반 Micro Framework
- 확장성 있는 설계를 지원함
- 예시 : Linked In이 Flask로 구현한 웹 애플리케이션
- 설치 : flask
- 자료 : https://flask-docs-kr.readthedocs.io/ko/latest/
- 별도의 환경을 만들어 줌

## 실습

### 1) flask 설치
- Pycharm으로 실행
- 별도의 가상환경이 필요함
- pycharm >> setting >> python interpreter >> + >> flask 검색 후 설치
![pycharm_onstall_flask](C:\Users\admin\Desktop\ku\pycharm_onstall_flask.PNG)

### 2) flask를 이용해 웹 브라우저에 보여줄 코드 작성
```python
from flask import Flask

# 플라스크 애플리케이션 생성
app = Flask(__name__)

# /(슬래시) 요청이 오면 처리하는 코드
# / 요청 : 도메인과 포트번호까지만 입력된 경우
@app.route('/')
def main():
    return 'Hello Flask!'

# 서버를 테스트용으로 실행
# Host를 127.0.0.1로 작성하면 로컬에서만 접속 가능
# Host를 0.0.0.0으로 작성하면 모든 곳에서 접속 가능
# port를 생략하면 포트를 5000번 할당함
# threaded = True 설정 시, 스레드로 요청 처리함
# debug = True 설정, 코드를 수정하면 자동으로 반영됨
    # 개발 시 debug = True
    # 운영 시 debug = False 로 반드시 변경할 것!
app.run(host = '0.0.0.0')
```
### 3) 코드 실행, 브라우저에서  접속
- 테스트
	- localhost:5000
	- 가상 아이피 : http://172.30.1.27:5000/ 
	- 가상 아이피라서 외부접속이 안 됨. 같은 wifi 이용하는 컴퓨터끼리 가능함
- 배포
	- ```flask run --host=0.0.0.0``` 명령 수행
	- 시작 파일 이름이 app.py여야 함
	- 파일이름 변경 : 환경변수에 FLASK_APP	속성에 파일명 설정

### 4) Flask에서 url 처리 방법

- 요청 경로가 서버에 도달하면 함수를 실행하고 결과를 출력함
    ```python
    @app.route('요청경로')
    def 함수이름:
        내용 작성
    ```
- 실습
    ```python
    # 추가
    # app.run 이전에 작성해야 함.
    @app.route('/cats')
    def cats():
        return '고양이 페이지'
    ```
- 확인 링크
	- http://172.30.1.27:5000/cats
- 서버가 재실행이 안 된 경우 404 error 뜰 수 있음!
	- debug = True로 설정해두면 새로 실행하지 않아도 수정된 코드를 반영함
	```python
	app.run(host = '0.0.0.0', debug = True)
	```

### 5) url의 일부분을 변수로 사용하기
- 최근의 웹 프로그래밍에서 많이 이용함
- 블로그형 게시판에서 상세보기에 주로 이용
- ```/url/<변수이름>```의 형태로 작성함

	```python
	# url의 일부분을 변수에 저장하여 사용
    # <berry>에서 berry는 변수임
    @app.route('/musical/<berry>')
    # 변수니까 매개변수 넣어줌
    def musical_b(berry):
        # 실제 페이지에서는 berry가 아니라 사용자가 입력한 매개변수를 출력함
        return berry
  
    # <int:num> 처럼 타입을 지정할 수 있음
    @app.route('/tistory/<int:num>')
    def tistory(num):
        return str(num)
  ```

## 2. Parameter 처리
- parameter : 클라이언트가 서버에 전송하는 데이터
- 처리 내부에서는 parameter 대신 argument란 용어를 사용하기도 함
- Web Programming에서는 Query String이라고도 함

### 1) Parameter 전송 방식
- get
	- parameter를 url 뒤에 붙여서 전송함
	- ```url + 이름=값 & 이름=값```의 형식으로 전송
	- 글자 수에 제한이 있음
	- 이름, 값이 그대로 드러남. 보안이 안 됨.
	- 자동 재전송 기능이 있음!
- post
	- parameter를 요청의 헤더에 숨겨서 전송함
	- form이나 javascript를 이용해서 전송함
	- 글자 수에 제한이 없고 보안이 우수함
	- 자동 재전송 기능이 없음
- put
	- post와 동일
- delete
	- post와 동일
- 최근의 웹프로그래밍은 요청을 명확하게 구분하기 위해 다음 규칙을 따름
	- 데이터를 삽입하는 경우 post
	- 수정하는 경우 put
	- 삭제하는 경우 delete

### 2) Parameter 처리
- request 전역객체 이용함
- request.method를 호출하면 파라미터 전송 방식이 문자열로 리턴됨
  - 요청을 처리할 때 methods에 처리방식을 기재하면 처리 방식이 맞을 때만 함수가 호출됨
- request.from을 호출하면 MultiDict로 리턴함
	- 단, 파일이 포함된 경우는 files를 호출해야 함
- request.args : url에 넘어온 파라미터를 MultiDict로 리턴함
- cookies : 쿠키 정보를 리턴
	- 고객의 정보를 브라우저에 저장하여 서버가 요청할 때 전달하는 방식
	- 보안 취약성이 의심되어 예전에는 잘 사용하지 않았으나, 요즘은 사용함
	- 고객의 웹상 동선을 추적하는 데 이용함
- headers : 헤더 정보를 리턴

## 2. 템플릿 엔진 (템플릿 렌더링)
- Flask에서는 다음 요청 처리 메소드를 리턴하여 파일을 출력함
	```python
	render_template('출력할 파일 경로')
	```
- template 디렉토리 >> index.html 파일
    ```python
    # template 디렉토리에 있는 파일을 출력해보자
    @app.route('/')
    def main():
        return render_template('index.html')
    
    # 파일 업로드
    @app.route('/upload', methods=['GET', 'POST'])
    def upload():
        # 파일 이름 변수에 저장
        f = request.files['file']
        # 파일을 서버에 저장
        f.save(f.filename)
        return f.filename + '업로드 성공'
	# 디렉토리에 파일 업로드 되는지 확인
    ```


## 3. REST API
- Full Stack 기술에서 중요한 기술
  - 서버에서 데이터를 넘기는 것
  - 클라이언트에서는 이 데이터를 가져와서 출력하는 것
  - 웹 클라이언트는 ajax로 구현
- ajax란?
	- Asynchronous JAvascript Xml
	- 비동기적으로 데이터를 가져오는 것
	- 네이버에서 각 화면이 부분적으로 갱신되는 걸 ajax로 구현함
- REST API는 서버에서 클라이언트에게 출력 대신 데이터를 넘겨주는 방식
	- 많이 사용되는 데이터 포맷 : json, xml(과거)
	- json
		- javascript object notation
		- 자바스크립트 객체 표현법. 파이썬도 동일함.
	- xml
		- eXtensible MArkup Language
		- 태그를 사용자가 해석

### 1) json 표기법
- 컴퓨터 친화적인 표기법
  Array : []
  Object : {}
    ```json
    {'data':[{'name':'adam', 'age':22}, {'name':'Rusia', 'age':29}]}
    ```
### 2) xml 표기법
- json보다 사람이 읽기 쉽지만 데이터 용량이 좀 더 커서 최근에는 json을 이용함
    ```xml
    <datas>
        <data>
            <name>Adam</name>
            <age>22</age>
        </data>
        <data>
            <name>Rusia</name>
            <age>29</age>
        </data>
    </datas>
    ```
### 3) 예시
- 각 신문사 RSS 클릭
	- list API 제공함
	- list API : 기사를 json 파일 형태로 제공

#### 405 에러 : GET, POST 따옴표 유의하기

### 4) json 출력
- jsonify에 데이터를 입력하고 리턴하면 됨

    ```python
    # json 출력
    # jsonify에 데이터 입력 후 리턴함
    from flask import jsonify
    @app.route('/json')
    def json():
        data = {'data':[{'name':'adam', 'age':22}, {'name':'Rusia', 'age':29}]}
        return jsonify(data)
    ```
### 5) xml 출력
- xml 문자열을 생성하고 return할 때 다음과 같이 리턴함
	```return data, {'Content-Type':'text/xml'}```
	```python	
    # xml 출력
    @app.route('/xml')
    def xml():
        data = '<persons>'
        data += '<person><name>Adam</name><age>22</age></person>'
        data += '<person><name>Mobam</name><age>27</age></person>'
        data += '</persons>'
        return data, {'Content-Type':'text/xml'}
  ```

## 4. 서버의 데이터 출력
- 서버에서 html에게 데이터를 넘기고자 할 때 다음을 리턴하여 출력함
	```python
	return render_template('템플릿 파일', 데이터이름 = 실제데이터)
	```
- html에서 출력할 때는 ```{{변수명}}```을 쓰자
- for문 사용 가능
	- 단, 데이터가 list인 경우만 가능함
	```python
	{% for 개별요소 in list명 %}
	내용
	# 닫는 코드
	{% endfor %}
	```
	- 반복문 안에서는 loop.속성이름을 이용해서 반복횟수, 첫번째, 마지막 순서를 구별할 수 있음
- if 사용 가능
	```python
	{ % if 조건 % }
		실행 코드
	{ % elif 조건 % }
		실행 코드
	{ % else % }
		실행 코드
	# 닫는 코드
	{% endif %}
	```
## 5. Web Application의 구조
- 요청(Request) >> Web Server >> Application Server >> 응답(Response)

### MVC 패턴
- 플라스크와 장고의 용어가 다르므로 유의하자!

- Model View Controller(장고에서 Model View Templat)
    - 참고 : https://opentutorials.org/module/3669/22003

- Appplication을 역할에 따라 구분해서 구현하는 것
    - Model(장고에서도 Model)
	    - 데이터를 만들어내는 것
    - View(장고에서 Template)
	    - 요청을 보내는 페이지 / 응답 페이지
    - Controller(장고에서 View)
        - 요청이 오면 작업을 처리하도록 메소드 호출하고
        - 응답을 만들어서 View에 전송하는 역할

#### clean code 구현 방법 소개
- 역할을 나눠 구현하는 경우
    - 디자이너와 개발자가 동시 개발이 가능함
    - 유지보수가 편리해짐

- 코드를 나누는 기준 : business logic / common concern
	- AOP(관점 지향 프로그래밍, Aspect Oriented Programming)
	- business logic
		- 업무처리를 위해서 사용되는 코드
		- 인케이스는 딱 이 알맹이 제공.
	- common concern
		- 공통 관심 사항. 업무처리 이외의 작업들. 로깅 등.
		- 더존 정보보호, sk는 패키지 sw를 만들어서 제공

## 6. 프로젝트의 기본 구조
- DAO (Data Access Object - Model)
- Service
	- 사용자의 요청을 처리해주는 클래스
- Controller
	- 요청 받고, 필요한 Business Logic을 호출하고,
	- 결과를 응답으로 만들어서, 출력할 파일에 전송함
- 실무
	- 클라이언트의 요구사항을 빈 클래스와 메소드로 먼저 구성함
    ```python
    회원가입
    join 요청 - def register() : 회원가입
	  def register(**info):
		pass
		return bool
    ```
- View (사용자에게 보여질 파일)

## 7. MySQL 연동
### 1) DB 준비 - MySQL
- 필요한 테이블과 샘플 데이터 작업 준비
- MySQL 다운로드
	- https://dev.mysql.com/downloads/
 	- MySQL Community Server 설치
	- 중간에 Excute 클릭 (Next 누르면 MySQL 없이 설치되는 수가 있음...)
	- 비번 : 9876
	- 작은 회사, 동양 네트웍스에서는 MySQL 이용함
- DBeaver에서 DB 생성
	- [파일] >> [새로 만들기] >> [DB 연결] >> MySQL 선택
		- MySQL 2개 깔아 쓰고 싶을 때 Port 번호 바꿈
	- 새로 만든 접속을 선택하고 마우스 오른쪽을 눌러서 [연결] 선택
		- 아무 것도 안 뜨면 잘 된 것
		- 에러 메시지 뜨면 비밀번호 확인, MySQL 잘 설치 되었는지 확인하자

- MySQL은 DB 단위로 작업함
	```sql
	show database DB이름; DB생성
	drop database DB이름; DB삭제
	use DB이름; DB사용
	
	# 테이블 생성
	Create table 테이블이름(
		컬럼이름 자료형 제약조건;
		컬럼이름 자료형 제약조건;
		제약조건;
		)
	# 테이블 수정
	alter table 테이블이름 작업;
	
	# 테이블 삭제
	## 삭제가 안 되는 경우는 다른 테이블에서 참조하는 경우임
	drop table 테이블이름
	
	# 데이터 삽입
	insert into 테이블이름(컬럼이름 나열) values(값을 나열);
	테이블을 만들 때 사용한 모든 컬럼에서 값을 대입할 때는 컬럼이름을 생략해도 	
	# 데이터 수정
	update 테이블이름 set 수정할내용 where 수정할 조건;
	# 데이터 삭제
	delete from 테이블이름 where 삭제조건;
	
	# 데이터 조회
	select 조회할 컬럼 나열
	from 조회할 테이블 이름
	where 조회할 조건
	groupby 그룹화할 컬럼나열
	having (groupby 이후의) 조건
	orderby 정렬할 컬럼과 방법을 나열
	```
#### 실습 코드 - DB 만들기
~~~sql
```
create database cat;

show databases;

use cat;

create table item(
itemid int,
itemname varchar(20),
price int,
description varchar(20),
pictureurl varchar(20),
primary key(itemid)
);

insert into item (itemid, itemname, price, description, pictureurl)
values(1, 'Lemon', 500, 'Sangcom', 'lemon.jpg');

insert into item (itemid, itemname, price, description, pictureurl)
values(2, 'Cherry', 700, 'Angcom', 'cherry.jpg');

insert into item (itemid, itemname, price, description, pictureurl)
values(3, 'Grapefruits', 1000, 'SSepssul', 'grapefruits.jpg');

select * from item;
```
~~~

### 2) 프로젝트 생성 ■■■
- pycharm에서 프로젝트 생성 > flask 설치
	- 라이브러리 설치 방법 :
	 	- 파일 > settings > 프로젝트 이름 > + 설치할 라이브러리 이름 검색 > 패키지 설치
	
- model의 역할을 수행할 model.py 파일 생성
- controller의 역할을 수행할 controller.py 파일 생성
- view들의 모임 역할을 수행할 templates 경로 생성

### 3) model.py
- model.py 파일에 DB 작업 관련 클래스 생성
- MySQL을 사용하기 위해 pymysql 패키지를 설치함
- DB 접속/해지 메소드
	```python
	import pymysql
  
    class Dao:
        # 데이터베이스 접속 메소드
        def connect(self):
            self.con=pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     passwd='9876',
                                     db='cat',
                                     charset='utf8')
            self.cursor=self.con.cursor()
  
        # 데이터베이스 연결을 해제하는 메소드
        def close(self):
            self.con.close()
  
        # 테이블의 전체 데이터를 불러오는 메소드
        def selectall(self):
            self.connect()
            # 수행할 SQL 문장 생성
            self.execute('select * from item')
            # 실행
            data = self.cursor.fetchall()
            # 데이터를 리스트로 변환하자
            cat_list = []
            for imsi in data:
                dic = {}
                dic['itemid'] = imsi[0]
                dic['itemname'] = imsi[1]
                dic['price'] = imsi[2]
                cat_list.append(dic)
            self.close()
            return cat_list
  ```
### 4) controller.py
~~~python
```python
from flask import Flask, request, render_template
import model

app = Flask(__name__)

@app.route('/')
def index():
    dao = model.Dao()
    # 데이터 가져오기
    data = dao.selectall()
    # 여기서 index 파일의 변수명을 data로 정해준 것
    # flask 프레임워크가 알아서 착착 처리해줌
    return render_template('index.html', data=data)

# 서버 실행
app.run(host='0.0.0.0', debug=True)
```
~~~
### 5) index.html
- templates 디렉토리에 index.html 파일 만들고, 전달된 데이터 출력하기
- index.html 파일 확인해보고 싶으면 controller.py 파일 실행하면 됨
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>고양이용 장난감 모음</title>
    </head>
    <body>
        <h2>장난감 목록</h2>
        <table border="1">
            <tr class="header">
                <th align="center" width="80">상품아이디</th>
                <th align="center" width="320">상품이름</th>
                <th align="center" width="100">가격</th>
            </tr>
            <!--
            여기서 data는 controller.py 파일의 data=data 부분 그 data
            그럼 controller에서 data라고 이름 짓고 여기서 data를 열어보는 건가?
            맞음 ! flask 프레임워크가 @app.route() 불러서 알아서 착착 처리해준 것-->
    
            {% for item in data %}
                <tr class="record">
                    <td align="center">{{item.itemid}}</td>
                    <td align="center">{{item.itemname}}</td>
                    <td align="right">{{item.price}}원</td>
                </tr>
            {%endfor%}
        </table>
    </body>
    </html>
    ```




---
# 다음 시간
# MySQL
# MongoDB