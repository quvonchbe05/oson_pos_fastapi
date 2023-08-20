from fastapi import APIRouter, HTTPException, Depends, Response
from api.models.models import User
from sqlalchemy import select, insert, update, delete
from api.db.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.users import UserCreateSchema, UserEditSchema
from passlib.hash import pbkdf2_sha256

router = APIRouter(
    prefix="/users",
    tags=[
        "Users",
    ],
)


@router.get("/list")
async def user_list(session: AsyncSession = Depends(get_async_session)):
    stmt = select(User)
    users = await session.scalars(stmt)
    return users.all()


@router.get("/detail/{user_id}")
async def user_detail(user_id: str, session: AsyncSession = Depends(get_async_session)):
    stmt = select(User).where(User.id == user_id)
    users = await session.scalar(stmt)
    return users


@router.post("/create")
async def user_create(
    new_user: UserCreateSchema, session: AsyncSession = Depends(get_async_session)
):
    # Check if the email is already registered
    db_email_query = select(User).where(User.email == new_user.email)
    db_email = await session.scalar(db_email_query)
    if db_email:
        raise HTTPException(status_code=400, detail="This email is already registered.")

    # Check if the username is already registered
    db_username_query = select(User).where(User.username == new_user.username)
    db_username = await session.scalar(db_username_query)
    if db_username:
        raise HTTPException(
            status_code=400, detail="This username is already registered."
        )

    stmt = insert(User).values(
        name=new_user.name,
        email=new_user.email,
        username=new_user.username,
        password=pbkdf2_sha256.hash(new_user.password),
    )
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.put("/edit/{user_id}")
async def user_edit(
    user_id: int,
    new_user: UserEditSchema,
    session: AsyncSession = Depends(get_async_session),
):
    # Check if the email is already registered
    db_email_query = select(User).where(User.email == new_user.email)
    db_email = await session.scalar(db_email_query)
    if db_email:
        raise HTTPException(status_code=400, detail="This email is already registered.")

    # Check if the username is already registered
    db_username_query = select(User).where(User.username == new_user.username)
    db_username = await session.scalar(db_username_query)
    if db_username:
        raise HTTPException(
            status_code=400, detail="This username is already registered."
        )

    stmt = (
        update(User)
        .values(
            name=new_user.name,
            email=new_user.email,
            username=new_user.username,
            password=pbkdf2_sha256.hash(new_user.password),
        )
        .where(User.id == user_id)
    )
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}


@router.delete("/delete/{user_id}")
async def user_edit(user_id: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(User).where(User.id == user_id)
    await session.execute(stmt)
    await session.commit()

    return {"status": "success"}
