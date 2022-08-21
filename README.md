# drf_ai_mulgam_backend
<aside>
💡 프로젝트명

</aside>

Mulgam

<aside>
💡 아키텍처

</aside>

- 사용 기술
    
    Python, Django, DRF
    
- 개발 환경
    - 웹 개발 환경
        - django_restframework
        - python
        - vsc **or** pycharm
    - 인공지능 개발 환경
        
        파이참
        

 

<aside>
💡 기능

</aside>

1. 로그인 / 회원가입 
    - 회원가입, 로그인
        - 실패시 , 안내문구 삽입
        - 비로그인 시 Gallery1, Gallery2 조회만 가능
        - 로그인 시 사진 올리기와 내가 올린 사진 보기 가능
    - 로그아웃 기능
    
2. Introduce
    - 페이지 소개 글
        - 첫화면 Introduce ( 팀원 소개 및 프로젝트 소개 )
    
3. Gallery 1
    - 기능1 (**유명 화가의 화풍을 따라하는 인공지능)**
        - 비로그인 시 로그인 페이지로 이동
    - 만들어진 그림들 보여줌

1. Gallery 2  
    - 기능 2 (**Neural Style Transfer)**
        - 비로그인 시 로그인페이지로 이동
    - 만들어진 그림들 보여줌

1. 마이 페이지
    - 내가 만든 그림들 보여줌
    
2.  댓글 모달
    - 그림 클릭 시 댓글 모달
    

---

<aside>
💡 와이어프레임

</aside>

### 로그인 / 회원가입

![로그인.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/90fce6dd-1e2a-47d1-95e9-3016c537b77d/로그인.png)

![회원가입.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51b82863-35c1-41aa-8517-7cbc85b2f436/회원가입.png)

### introduce

![메인 - Introduce.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5ce7e14-aebb-4d9c-8e1a-d55ce4c211cd/메인_-_Introduce.png)

### mypage

![모달 - _Mypage.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a60974d-d1e8-4910-8ed7-d056f8bb534e/모달_-__Mypage.png)

### gallery1

![모달 - Gallery 1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/985bf7ab-e67e-48f3-913f-cf82cfa67ba9/모달_-_Gallery_1.png)

### gallery2

![모달 - Gallery 2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/030369f9-34a0-4d21-bf06-20d458fa53c7/모달_-_Gallery_2.png)
