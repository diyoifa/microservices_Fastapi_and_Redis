from fastapi import FastAPI, status, HTTPException
from middlewares.setup_cors import setup_cors
from routers import product_router

app = FastAPI(
    title='Inventory API',
    description='Inventory API',
    version='1.0.0'
)

#MIDDLEWARES
setup_cors(app)

#ROUTERS
app.include_router(product_router.router)

