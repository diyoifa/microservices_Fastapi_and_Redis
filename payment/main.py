from fastapi import FastAPI, status, HTTPException
from middlewares.setup_cors import setup_cors
from routers import order_route

app = FastAPI(
    title='Payment API',
    description='Payment API',
    version='1.0.0'
)

#MIDDLEWARES
setup_cors(app)

#ROUTERS
app.include_router(order_route.router)
