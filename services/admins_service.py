from domain.admin import Schedule
from repository import admins_repository
from lib import whosoff_requestor

def create_schedule(schedule: Schedule):
    return admins_repository.create_schedule(schedule)


def edit_schedule(schedule: Schedule):
    return admins_repository.update_schedule(schedule)


def get_schedule(id: int):
    return admins_repository.get_schedule(id)


def get_schedules():
    return admins_repository.get_schedules()


def get_whosoff_schedules(start_date: str, end_date: str):
    return whosoff_requestor.get_days_off(start_date, end_date)


def get_whosoff_staff():
    return whosoff_requestor.get_staff()
