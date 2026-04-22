# 🧠 Health Risk Prediction API

> 개인 건강 데이터를 기반으로
> 당뇨병 / 고혈압 위험도를 예측하는 AI API 서비스

---

## 📌 프로젝트 소개

이 프로젝트는 사용자의 건강 프로필을 기반으로
AI 모델을 활용하여 **당뇨병 및 고혈압 위험도를 예측**하는 백엔드 API 서비스입니다.

* JWT 기반 인증 시스템
* FastAPI 기반 비동기 API
* SQLAlchemy ORM 기반 데이터 관리
* LLM 기반 위험도 예측

---

## 🚀 주요 기능

### 1️⃣ 사용자 인증 (JWT)

* 로그인 시 Access Token 발급
* API 요청 시 토큰 검증

### 2️⃣ 건강 프로필 관리

* 사용자 건강 데이터 저장
* 개인별 프로필 조회

### 3️⃣ AI 위험도 예측

* 건강 데이터를 기반으로

  * 당뇨병 확률
  * 고혈압 확률
* LLM 모델 활용

### 4️⃣ 예측 결과 저장

* DB에 예측 결과 기록
* 모델 버전 관리

---

## 🏗️ 프로젝트 구조

```
risk_predict/
│
├── auth/                # 인증 (JWT, 비밀번호 처리)
├── database/            # DB 연결 및 ORM 설정
├── user/                # 사용자 및 건강 프로필
├── prediction/          # AI 예측 로직
│
├── config.py            # 환경 설정
├── main.py              # FastAPI 앱 실행
├── db.sqlite            # SQLite DB
```

---

## ⚙️ 기술 스택

| 분야       | 기술         |
| -------- | ---------- |
| Backend  | FastAPI    |
| Database | SQLite     |
| ORM      | SQLAlchemy |
| Auth     | JWT        |
| Async    | asyncio    |
| AI       | LLM 기반 예측  |

---

## 🔄 API 흐름

```
[사용자 로그인]
        ↓
[JWT 발급]
        ↓
[건강 프로필 등록]
        ↓
[/predictions 요청]
        ↓
[DB에서 프로필 조회]
        ↓
[LLM 호출 → 위험도 예측]
        ↓
[결과 DB 저장]
        ↓
[응답 반환]
```

---

## 🧪 실행 방법

```bash
# 가상환경 실행
source .venv/bin/activate

# 서버 실행
uvicorn main:app --reload
```

접속:

```
http://127.0.0.1:8000/docs
```

---

## 🚨 Troubleshooting (문제 해결 기록)

---

### 1. 500 Internal Server Error (원인 불명)

#### 🔥 문제

* API 호출 시 500 에러 발생
* 터미널 로그 없음

#### 💡 원인

👉 로그를 찍지 않아 원인을 확인할 수 없었음

#### ✅ 해결

```python
print("1. 시작")
print("2. profile:", profile)
print("3. LLM 호출 전")
print("4. LLM 결과:", risk_prediction)
```

👉 실행 흐름을 추적해서 문제 위치 확인

---

### 2. UnboundLocalError (변수 접근 오류)

#### 🔥 문제

```
profile 변수 접근 불가
```

#### 💡 원인

👉 변수 선언 전에 사용

#### ✅ 해결

```python
profile = result.scalar()
print(profile)
```

---

### 3. SQLAlchemy 필드명 오류

#### 🔥 문제

```
invalid keyword argument
```

#### 💡 원인

```python
disbetes_probability  ❌ (오타)
```

#### ✅ 해결

```python
diabetes_probability  ✅
```

👉 ORM은 필드명 정확도가 매우 중요

---

### 4. DB 테이블 생성 안됨

#### 🔥 문제

* 테이블이 생성되지 않음 -> 3.번 문제로 필드명이 바뀌면서 테이블이 없었어 다시 생성해야했음.

#### 💡 원인

👉 init_db 실행 

#### ✅ 해결

```python
import asyncio
from prediction.models import HealthRiskPrediction
from database.orm import init_db

asyncio.run(init_db())
```
---

#### 🔥 문제

```
NoReferencedTableError 
```

#### 💡 원인

👉 참조 테이블(user)이 등록되지 않음 -> 테이블 등록 시 import 를 하지 않음.

#### ✅ 해결

```python
from user.models import User
```

👉 모든 모델을 import 해야 테이블 생성됨

---

### 6. JWT 설정 오류

#### 🔥 문제

```
validation error for Settings  
jwt_secret  
Extra inputs are not permitted
```

#### 💡 원인

👉class Settings:
    # JWT_SECRET 없음 ❌

#### ✅ 해결

```python
class Settings:
    JWT_SECRET: str 추가
```

---

### 7. FastAPI return 직렬화 문제

#### 🔥 문제

```python
return risk_prediction  ❌
```

#### 💡 원인

👉 LLM 객체는 JSON 변환 불가

#### ✅ 해결

```python
return new_prediction 
```
👉 FastAPI는 내부적으로  
`JSON.stringify 가능한 형태`만 응답 가능

---

### 8. Git 충돌 문제

#### 🔥 문제

```
merge conflict 발생
```

#### 💡 원인

👉 원격과 로컬 코드 불일치

#### 😅 해결

```bash
git push -f origin main
```

👉 빠르게 해결했지만 협업 시 위험
이번에는 혼자 작성한 코드 였기 때문에 일단 올리는 걸로 함.

---

