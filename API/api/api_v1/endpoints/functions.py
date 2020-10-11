from fastapi import APIRouter, HTTPException, status
from core.functions.ai import ai_core

import secrets
from typing import List, Optional


ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'


router = APIRouter()


def check_access_token(token, real_token=ACCESS_TOKEN):
    correct_token = secrets.compare_digest(token, real_token)
    if not correct_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login",
        )


@router.post("/auth", summary="Аунтификация пользователя. На вход подаётся почта и пароль. Возвращается токен авторизации.")
def create_submit(
        email: Optional[str] = None,
        password: Optional[str] = None,
):
    # Обращение к БД для проверки существования пользователя и правильности его пароля
    auth = True
    if email is not None and password is not None:
        if auth:
            return {
                'access_token': ACCESS_TOKEN,
                'refresh_token': ACCESS_TOKEN,
            }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect login",
    )


@router.post("/refresh_auth", summary="Обновление токена авторизации")
def create_submit(
        email: Optional[str] = None,
        refresh_token: Optional[str] = None,
):
    # Обращение к БД для проверки существования пользователя и правильности его пароля
    auth = True
    if email is not None:
        if auth:
            return {
                'access_token': ACCESS_TOKEN,
                'refresh_token': ACCESS_TOKEN,
            }

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect login",
    )


@router.post("/submit", summary="Получение данных об операции. AI валидация данных")
def create_submit(
        email: str,
        to: str,
        amount: float,
        message: Optional[str] = '',
        token: str = '',
        ai_token: Optional[str] = '',
):
    check_access_token(token)

    return {'fraud_prob': ai_core(amount, message, ai_token)}


