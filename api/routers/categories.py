from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db.db import get_async_session
from sqlalchemy import select, insert, update, delete
from api.models.models import Category
from api.schemas.categories import CategorySchema

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/list")
async def category_list(session: AsyncSession = Depends(get_async_session)):
    stmt = select(Category)
    categories = await session.scalars(stmt)
    return categories.all()


@router.get("/detail/{category_id}")
async def category_detail(
    category_id: int, session: AsyncSession = Depends(get_async_session)
):
    stmt = select(Category).where(Category.id == category_id)
    categories = await session.scalar(stmt)
    return categories


@router.post("/create")
async def category_create(
    new_category: CategorySchema, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Category).values(name=new_category.name)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.put("/edit/{categry_id}")
async def category_edit(
    category_id: int,
    new_category: CategorySchema,
    session: AsyncSession = Depends(get_async_session),
):
    stmt = (
        update(Category)
        .values(name=new_category.name)
        .where(Category.id == category_id)
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/delete/{categry_id}")
async def category_delete(
    category_id: int, session: AsyncSession = Depends(get_async_session)
):
    stmt = delete(Category).where(Category.id == category_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
