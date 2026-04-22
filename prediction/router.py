from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select

from auth.jwt import verify_user
from database.connection import get_session
from user.models import HealthProfile
from prediction.llm import predict_health_risk
from prediction.models import HealthRiskPrediction

print("1. 시작")

router = APIRouter(tags=["Prediction"])

@router.post(
    "/predictions",
    summary="당뇨병/고혈압 위험도 예측 API ",
    status_code = status.HTTP_201_CREATED,
)
async def predict_health_risk_handler(
    # 1) 데이터 입력(건강 프로필) -> 인증 토큰으로 id 가져오기
    # 인증 토큰 요구
    user_id = Depends(verify_user),
    session = Depends(get_session),
):
    # 2) 건강 프로필 조회
    stmt = (
        select(HealthProfile)
        .where(HealthProfile.user_id == user_id)
    )
    result = await session.execute(stmt)
    profile = result.scalar()

    print("2. profile:", profile)
    
    if not profile:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail="건강 프로필이 없습니다."
        )
    print("3. LLM 호출 전")
    # 3) 위험도 예측
    model_version = "gpt-5-mini"
    risk_prediction = await predict_health_risk(
        profile=profile, model_version=model_version
    )
    print(type(risk_prediction.diabetes_probability))
    print("4. LLM 결과:", risk_prediction)

    print("5. DB 저장 전")
    # 4) 결과 저장
    new_prediction = HealthRiskPrediction(
        user_id=user_id,
        diabetes_probability=risk_prediction.diabetes_probability,
        hypertension_probability=risk_prediction.hypertension_probability,
        model_version=model_version
    )
    session.add(new_prediction)
    await session.commit()
    await session.refresh(new_prediction)

    return new_prediction
