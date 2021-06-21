from domain.donation import Donation
from typing import Optional, List
from repository import donations_repository
from services import stripe_service

def create_donation(donation: Donation):
    return donations_repository.create_donations(donation)


def create_donation_intent(donation: Donation):
    return stripe_service.create_payment(donation.amount)


def get_donations(username: Optional[str], fundraiser_id: Optional[str]):
    return donations_repository.get_donations(username, fundraiser_id)


def get_donation_sums(usernames: List[int], fundraiser_id: str):
    return donations_repository.get_donations_amounts_for_users(usernames, fundraiser_id)
