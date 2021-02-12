from domain.fundraisers import Fundraiser
from repository import fundraiser_repository
from typing import Optional


def create_fundraiser(fundraiser: Fundraiser):
    return fundraiser_repository.create_fundraiser(fundraiser)


def update_fundraiser(fundraiser: Fundraiser):
    return fundraiser_repository.update_fundraiser(fundraiser)


def get_fundraiser(id: Optional[int], name: Optional[str]):
    return fundraiser_repository.get_fundraisers(name, id)
