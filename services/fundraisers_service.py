from domain.donation import Donation, DonationWithUser
from domain.fundraisers import Fundraiser, UserFundraiserEnrollment
from domain.user import UserSearch
from repository import fundraiser_repository
from typing import Optional, List
from services import donations_service, users_service

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
            user_ids.append(enrollment.user_id)
        people = donations_service.get_donation_sums(user_ids, fundraiser.id)
        for index, person in enumerate(people):
            user = users_service.get_user(UserSearch(user_id=person.user_id))
            people[index] = DonationWithUser(user=user[0],
                                             fundraiser_id=person.fundraiser_id,
                                             donor_first_name=person.donor_first_name,
                                             donor_last_name=person.donor_last_name,
                                             donor_comment=person.donor_comment,
                                             amount=person.amount,
                                             currency=person.currency)

        fundraiser.people = people
    return fundraisers


def enroll_user_to_fundraiser(user_fundraiser_enrollment: UserFundraiserEnrollment):
    return fundraiser_repository.enroll_user_in_fundraiser(user_fundraiser_enrollment)


def get_user_fundraiser_enrollments(user_id: Optional[int],
                                    fundraiser_id: Optional[int]) -> List[UserFundraiserEnrollment]:
    return fundraiser_repository.get_users_fundraisers(user_id, fundraiser_id)