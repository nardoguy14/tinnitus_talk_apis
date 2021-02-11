from fastapi import FastAPI
from controllers.users_controller import router as users_router
from controllers.donations_controller import donations_router
from controllers.fundraisers_controller import fundraisers_router
app = FastAPI()

app.include_router(users_router)
app.include_router(donations_router)
app.include_router(fundraisers_router)
