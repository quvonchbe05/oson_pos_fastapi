from fastapi import FastAPI, Depends
from api.routers.auth import router as auth_router
from api.routers.users import router as user_router
from api.routers.categories import router as categry_router
from api.routers.products import router as product_router
from api.routers.basket import router as basket_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(categry_router)
app.include_router(product_router)
app.include_router(basket_router)

