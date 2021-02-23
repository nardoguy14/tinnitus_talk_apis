from domain.fundraisers import Fundraiser, UserFundraiserEnrollment
from repository import fundraiser_repository
from typing import Optional, List
from services import donations_service

def create_fundraiser(fundraiser: Fundraiser):
    id = fundraiser_repository.create_fundraiser(fundraiser)
    fundraiser.id = id
    return fundraiser_repository.create_fundraiser_details(fundraiser)


def update_fundraiser(fundraiser: Fundraiser):
    return fundraiser_repository.update_fundraiser(fundraiser)


def get_fundraiser(id: Optional[int], name: Optional[str]):
    fundraisers = fundraiser_repository.get_fundraisers(name, id)
    for fundraiser in fundraisers:
        fundraiser.details = fundraiser_repository.get_fundraisers_details(fundraiser.id)
        user_fundraiser_enrollments = get_user_fundraiser_enrollments(user_id=None, fundraiser_id=fundraiser.id)
        user_ids = []
        for enrollment in user_fundraiser_enrollments:
            print(enrollment)
            user_ids.append(enrollment.user_id)
        fundraiser.people = donations_service.get_donation_sums(user_ids, fundraiser.id)
    return fundraisers


def enroll_user_to_fundraiser(user_fundraiser_enrollment: UserFundraiserEnrollment):
    return fundraiser_repository.enroll_user_in_fundraiser(user_fundraiser_enrollment)


def get_user_fundraiser_enrollments(user_id: Optional[int],
                                    fundraiser_id: Optional[int]) -> List[UserFundraiserEnrollment]:
    return fundraiser_repository.get_users_fundraisers(user_id, fundraiser_id)