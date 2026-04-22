from pydantic import BaseModel

# 회원가입 요청에 필요한 데이터 형식
class SignUpRequest(BaseModel):
    email: str
    password: str  # plain text

# 로드인에 필요한 데이터 형식
class LogInRequest(BaseModel):
    email: str
    password: str   

# 공유해서 써도 되지만 구체적으로 이름을 짓고, 
# 나중에 데이터를 추가할 수 있는데 각자가 다른 모양을 나타낼 수 있으니

# 건강 프로필 생성에 필요한 데이터 형식
class HealthProfileRequest(BaseModel):
    age: int
    height_cm: float
    weight_kg: float
    smoking: bool
    exercise_per_week: int