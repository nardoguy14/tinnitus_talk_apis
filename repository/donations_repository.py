from typing import Optional, List
from domain.donation import Donation
import mysql.connector
from repository.base_repository import BaseRepository


def create_donations(donation: Donation):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO donations (
        user_id,
        donor_first_name,
        donor_last_name,
        donor_comment,
        fundraiser_id,
        amount,
        currency
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (donation.user_id, donation.donor_first_name, donation.donor_last_name,
               donation.donor_comment, donation.fundraiser_id, donation.amount, donation.currency)
        base_repo.execute(sql, val)
        return {"result": "saved"}


def get_donations(username: Optional[str], fundraiser_id: Optional[str]):
    with BaseRepository() as base_repo:
        query_params = []
        if username:
            query_params.append(" username = %s ")
        if fundraiser_id:
            query_params.append(" fundraiser_id = %s ")

        query_str = " AND ".join(query_params)

        query = ("""SELECT 
                        user_id,
                        donor_first_name,
                        donor_last_name,
                        donor_comment,
                        fundraiser_id,
                        amount,currency 
                    FROM donations 
                """
                f"WHERE {query_str}")
        params = [username, fundraiser_id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))
        base_repo.execute(query, filtered_params)

        results = []
        for (user_id,
             donor_first_name,
             donor_last_name,
             donor_comment,
             fundraiser_id,
             amount,
             currency) in base_repo:
            results.append(Donation(user_id=user_id, donor_first_name=donor_first_name,
                                    donor_last_name=donor_last_name, donor_comment=donor_comment,
                                    fundraiser_id=fundraiser_id, amount=amount, currency=currency))

        return results


def get_donations_amounts_for_users(user_ids: List[int], fundraiser_id: str):
    with BaseRepository() as base_repo:
        if len(user_ids) == 0:
            return []
        print(user_ids)
        print(fundraiser_id)
        format_strings = ','.join(['%s'] * len(user_ids))
        print(format_strings)
        user_ids_str = "user_id in (%s)" % format_strings
        query = (f"""
                    select 
                        user_id, 
                        SUM(amount) as total_donation from donations
                    where {user_ids_str} AND fundraiser_id = %s
                    group by (user_id) 
                """)
        print(query)
        user_ids.append(fundraiser_id)
        print(user_ids)
        filtered_params = tuple(list(filter(lambda x: x != None, user_ids)))
        base_repo.execute(query, filtered_params)

        results = []
        for (
                user_id,
                total_donation
            ) in base_repo:
            results.append(Donation(user_id=user_id, donor_first_name=None,
                                    donor_last_name=None, donor_comment=None,
                                    fundraiser_id=fundraiser_id, amount=total_donation,
                                    currency="USD"))
        print(results)
        return results
