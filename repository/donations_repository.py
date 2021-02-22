from typing import Optional
from domain.donation import Donation
import mysql.connector
from repository.base_repository import BaseRepository


def create_donations(donation: Donation):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO donations (
        username,
        donor_first_name,
        donor_last_name,
        donor_comment,
        fundraiser_id,
        amount,
        currency
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        val = (donation.username, donation.donor_first_name, donation.donor_last_name,
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
                        username,
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
        for (username,
             donor_first_name,
             donor_last_name,
             donor_comment,
             fundraiser_id,
             amount,
             currency) in base_repo:
            results.append(Donation(username=username, donor_first_name=donor_first_name,
                                    donor_last_name=donor_last_name, donor_comment=donor_comment,
                                    fundraiser_id=fundraiser_id, amount=amount, currency=currency))

        return results
