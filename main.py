from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
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

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)
