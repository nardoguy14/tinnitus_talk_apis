from fastapi import FastAPI
from controllers.users_controller import router as users_router
from controllers.donations_controller import donations_router
from controllers.fundraisers_controller import fundraisers_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router)
app.include_router(donations_router)
app.include_router(fundraisers_router)
