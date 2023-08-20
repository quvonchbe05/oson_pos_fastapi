from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db.db import get_async_session
from sqlalchemy import select, insert, update, delete
from api.schemas.basket import BasketCreateSchema
from api.models.models import Basket, Product, Saled


router = APIRouter(
    prefix="/basket",
    tags=[
        "Basket",
    ],
)


@router.get("/list/{user_id}")
async def basket_list(user_id: str, session: AsyncSession = Depends(get_async_session)):
    stmt = select(Basket).where(Basket.user == user_id)
    products = await session.scalars(stmt)
    response = products.all()
    return response


@router.post("/create")
async def basket_create(
    new_basket: BasketCreateSchema, session: AsyncSession = Depends(get_async_session)
):
    stmt = insert(Basket).values(
        name=new_basket.name,
        count=new_basket.count,
        price=new_basket.price,
        total_price=str(int(new_basket.count) * int(new_basket.price)),
        user=new_basket.user,
    )
    await session.execute(stmt)
    await session.commit()
    return {"status": {"status": "success"}}


@router.post("/sale/{user_id}")
async def basket_sale(user_id: str, session: AsyncSession = Depends(get_async_session)):
    basket_query = select(Basket).where(Basket.user == user_id)
    basket = await session.scalars(basket_query)
    for b in basket:
        product = (
            update(Product)
            .values(amount=Product.amount - int(b.count))
            .where(Product.id == b.name)
        )
        await session.execute(product)
        await session.commit()
        product_query = select(Product).where(Product.id == b.name)
        pr = await session.scalar(product_query)
        save_to_saled = insert(Saled).values(
            name=pr.name,
            count=b.count,
            price=b.price,
            total_price=b.total_price,
            user=b.user,
        )
        await session.execute(save_to_saled)
        await session.commit()
        basket2 = delete(Basket).where(Basket.id == b.id)
        await session.execute(basket2)
        await session.commit()
    return {"status": "success"}


@router.delete("/delete/{user_id}/{product_id}")
async def basket_delete(
    user_id: str, product_id: int, session: AsyncSession = Depends(get_async_session)
):
    stmt = delete(Basket).where(Basket.user == user_id, Basket.id == product_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.delete("/refresh/{user_id}")
async def basket_refresh(
    user_id: str, session: AsyncSession = Depends(get_async_session)
):
    stmt = delete(Basket).where(Basket.user == user_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
