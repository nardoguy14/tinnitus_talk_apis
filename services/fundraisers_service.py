from domain.fundraisers import Fundraiser
from repository import fundraiser_repository


def create_fundraiser(fundraiser: Fundraiser):
    return fundraiser_repository.create_fundraiser(fundraiser)
