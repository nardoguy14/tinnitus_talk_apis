from typing import Optional
from domain.fundraisers import Fundraiser, UserFundraiserEnrollment, FundraiserDetails
from repository.base_repository import BaseRepository


def create_fundraiser(fundraiser: Fundraiser):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO fundraisers (
        name,
        description,
        address,
        city,
        state,
        zip,
        date_start,
        date_end
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (
               fundraiser.name,
               fundraiser.description,
               fundraiser.address,
               fundraiser.city,
               fundraiser.state,
               fundraiser.zip,
               fundraiser.date_start,
               fundraiser.date_end
        )

        base_repo.execute(sql, val)
        return base_repo.lastrowid


def create_fundraiser_details(fundraiser: Fundraiser):
    with BaseRepository() as base_repo:
        for detail in fundraiser.details:
            sql = """
            INSERT INTO fundraiser_details (
                fundraiser_id,
                title,
                detail
            ) VALUES (%s, %s, %s)"""
            val = (
                fundraiser.id,
                detail.title,
                detail.detail
            )
            base_repo.execute(sql, val)
        return {"result": "saved"}


def update_fundraiser(fundraiser: Fundraiser):
    with BaseRepository() as base_repo:
        sql = """UPDATE fundraisers 
        SET
        name = %s,
        description = %s,
        address = %s,
        city = %s,
        state = %s,
        zip = %s,
        date_start = %s,
        date_end = %s
        WHERE id = %s"""
        val = (
            fundraiser.name,
            fundraiser.description,
            fundraiser.address,
            fundraiser.city,
            fundraiser.state,
            fundraiser.zip,
            fundraiser.date_start,
            fundraiser.date_end,
            fundraiser.id
        )
        base_repo.execute(sql, val)
        return {"result": "updated"}


def get_fundraisers_details(id: Optional[int]):
    with BaseRepository() as base_repo:
        if id:
            query_str = f" WHERE fundraiser_id = %s"

        query = (f"""SELECT 
                        id,
                        fundraiser_id,
                        title,
                        detail
                    FROM fundraiser_details 
                    {query_str}  
                """)
        params = [id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))
        base_repo.execute(query, filtered_params)

        results = []
        for (
                id,
                fundraiser_id,
                title,
                detail
            ) in base_repo:
            results.append(FundraiserDetails(id=id, fundraiser_id=fundraiser_id,
                                             title=title, detail=detail))

        return results


def get_fundraisers(name: Optional[str], id: Optional[int]):
    with BaseRepository() as base_repo:
        query_params = []
        if name:
            query_params.append(" username LIKE %s ")
        if id:
            query_params.append(" id = %s ")

        query_str = " AND ".join(query_params)
        if name or id:
            query_str = f" WHERE {query_str}"

        query = ("""SELECT 
                        id,
                        name,
                        description,
                        address,
                        city,
                        state,
                        zip,
                        date_start,
                        date_end
                    FROM fundraisers 
                """
                 f"{query_str}")
        params = [name, id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))
        base_repo.execute(query, filtered_params)

        results = []
        for (
             id,
             name,
             description,
             address,
             city,
             state,
             zip,
             date_start,
             date_end) in base_repo:
            print(date_start)
            print(type(date_start))
            results.append(Fundraiser(id=id, name=name, description=description,
                                    address=address, city=city, state=state, zip=zip,
                                    date_start=date_start.strftime("%Y-%m-%d %H:%M:%S"),
                                    date_end=date_end.strftime("%Y-%m-%d %H:%M:%S")))

        return results


def enroll_user_in_fundraiser(user_fundraiser_enrollment: UserFundraiserEnrollment):
    with BaseRepository() as base_repo:
        sql = """
        INSERT INTO users_to_fundraisers (
            user_id,
            fundraiser_id,
            fundraiser_goal
        ) VALUES (%s, %s, %s)
        """

        val = (
            user_fundraiser_enrollment.user_id,
            user_fundraiser_enrollment.fundraiser_id,
            user_fundraiser_enrollment.fundraiser_goal_amount
        )

        base_repo.execute(sql, val)
        return {"result": "saved"}


def get_users_fundraisers(user_id: int):
    with BaseRepository() as base_repo:
        query = ("""
                    SELECT 
                        id,
                        user_id,
                        fundraiser_id,
                        fundraiser_goal
                    FROM users_to_fundraisers 
                    WHERE user_id = %s
                """
                )
        params = [user_id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))
        base_repo.execute(query, filtered_params)

        results = []
        for (
                id,
                user_id,
                fundraiser_id,
                fundraiser_goal
        ) in base_repo:
            results.append(UserFundraiserEnrollment(
                user_id=user_id, fundraiser_id=fundraiser_id, fundraiser_goal_amount=fundraiser_goal))
        return results
