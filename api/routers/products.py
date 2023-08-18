from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.db.db import get_async_session
from sqlalchemy import select, insert, update, delete
from api.models.models import Product, Category
from api.schemas.products import ProductSchema


router = APIRouter(
    prefix='/products',
    tags=["Products", ]
)

@router.get('/list')
async def product_list(session: AsyncSession = Depends(get_async_session)):
    stmt = select(Product)
    products = await session.scalars(stmt)
    response = products.all()
    for product in response:
        category_stmt = select(Category).where(Category.id == product.category_id)
        product.category = await session.scalar(category_stmt)
    return response


@router.get('/detail/{product_id}')
async def product_detail(product_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = select(Product).where(Product.id == product_id)
    product = await session.scalar(stmt)
    category_stmt = select(Category).where(Category.id == product.category_id)
    product.category = await session.scalar(category_stmt)
    return product


@router.post('/create')
async def product_create(new_product: ProductSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Product).values(
        name=new_product.name,
        amount=new_product.amount,
        price=new_product.price,
        sale_price=new_product.sale_price,
        bar_code=new_product.bar_code,
        category_id=new_product.category_id,
    )
    await session.execute(stmt)
    await session.commit()
    return "success"


@router.put('/edit/{product_id}')
async def product_create(product_id: int, new_product: ProductSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Product).values(
        name=new_product.name,
        amount=new_product.amount,
        price=new_product.price,
        sale_price=new_product.sale_price,
        bar_code=new_product.bar_code,
        category_id=new_product.category_id,
    ).where(Product.id == product_id)
    await session.execute(stmt)
    await session.commit()
    return "success"


@router.delete('/delete/{product_id}')
async def product_delete(product_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Product).where(Product.id == product_id)
    await session.execute(stmt)
    await session.commit()
    return "success"