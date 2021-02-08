from fastapi import FastAPI
from controllers.users_controller import router as users_router

app = FastAPI()


app.include_router(users_router)