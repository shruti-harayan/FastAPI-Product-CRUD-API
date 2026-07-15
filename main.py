from fastapi import FastAPI
from src.routes.ProductRoute import productRoutes

app=FastAPI(
    title="FastAPI starting out",
    description="I am learning fastapi from youtube"
)


@app.get("/home")
def home():
    return {
        "message":"Success"
    }


app.include_router(productRoutes,prefix="/product")