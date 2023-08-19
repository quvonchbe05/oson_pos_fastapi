from fastapi import APIRouter, HTTPException, Depends
from api.models.models import User
from api.db.config import SECRET_KEY
from sqlalchemy import select
from api.db.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from passlib.hash import pbkdf2_sha256


router = APIRouter(
    tags=['Auth'],
    prefix='/api/auth'
)


@router.post("/login")
async def login(username: str, password: str, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.username == username)
    user = await session.scalar(stmt)
    if user and pbkdf2_sha256.verify(password, user.password):
        return {
                "id": str(user.id),
                "name": user.name,
                "username": user.username,
                "email": user.email,
                "is_admin": user.is_admin,
            }
    else:
        raise HTTPException(status_code=401, detail="Incorrect username or password.")
