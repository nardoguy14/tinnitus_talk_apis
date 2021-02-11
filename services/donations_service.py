from domain.donation import Donation
from repository import donations_repository


def create_donation(donation: Donation):
    return donations_repository.create_donations(donation)


def get_donations(username: str):
    return donations_repository.get_donations(username)
