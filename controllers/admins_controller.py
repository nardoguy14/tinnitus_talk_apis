from fastapi import APIRouter
from domain.admin import Schedule
import logging
from services import admins_service

logger = logging.getLogger()
logger.setLevel(logging.INFO)

admins_router = APIRouter()


@admins_router.post("/admins/schedule")
async def create_schedule(schedule: Schedule):
    return admins_service.create_schedule(schedule)


@admins_router.put("/admins/schedule")
async def edit_schedule(schedule: Schedule):
    admins_service.edit_schedule(schedule)
    return schedule


@admins_router.get("/admins/schedules")
async def get_schedules():
    return admins_service.get_schedules()


@admins_router.get("/admins/schedule/{id}")
async def get_schedule(id: int):
    return admins_service.get_schedule(id)


@admins_router.get("/admins/whosoff/schedules")
async def get_whosoff_schedules(start_date: str, end_date: str):
    return admins_service.get_whosoff_schedules(start_date, end_date)


@admins_router.get("/admins/whosoff/staff")
async def get_whosoff_staff():
    return admins_service.get_whosoff_staff()
