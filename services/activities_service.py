from domain.activity import Activity
from repository import activities_repository


def create_activity(activity: Activity):
    return activities_repository.create_activity(activity)


def get_activities(fundraiser_id: int):
    return activities_repository.get_activies(fundraiser_id)
