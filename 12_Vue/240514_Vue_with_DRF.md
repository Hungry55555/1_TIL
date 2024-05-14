# Authentication with DRF
## 개요
### 시작하기 전에
* 인증 로직 진행을 위해 User 모델 관련 코드 활성화
* user ForeignKey 주석 해제
```py:articles/models.py

class Article(models.Model):
    user = models.ForeignKey(
      settings.AUTH_USER_MODEL, on_delete = models.CASCADE
    )
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

* serializers의 read_only_fields 주석 해제


## 인증
## 인증 체계 설정
## Token 인증 설정
## Dj-Rest-Auth 라이브러리
## Token 발급 및 활용
## 권한 정책 설정
## IsAuthenticated 권한 설정

# Authentication with Vue
## 회원가입
## 로그인
## 요청과 토큰
## 인증 여부 확인
## 기타 기능 구현
