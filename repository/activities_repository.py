from typing import Optional
from domain.activity import Activity
from repository.base_repository import BaseRepository


def create_activity(activity: Activity):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO activities (
            fundraiser_id,
            distance,
            activity_type,
            date_start,
            created_at
        ) VALUES (%s, %s, %s, %s, %s)"""
        val = (
            activity.fundraiser_id,
            activity.distance,
            activity.activity_type,
            activity.date_start,
            activity.created_at
        )
        base_repo.execute(sql, val)
        return base_repo.lastrowid


def get_activies(fundraiser_id: int):
    with BaseRepository() as base_repo:
        query_params = []
        if fundraiser_id:
            query_params.append(" fundraiser_id = %s ")

        query_str = " AND ".join(query_params)
        if fundraiser_id:
            query_str = f" WHERE {query_str}"

        query = ("""
                    SELECT 
                        fundraiser_id,
                        distance,
                        activity_type,
                        date_start,
                        created_at
                    FROM activities 
                """
                f"""{query_str}"""
                )
        params = [fundraiser_id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))
        base_repo.execute(query, filtered_params)

        results = []
        for (
                fundraiser_id,
                distance,
                activity_type,
                date_start,
                created_at
        ) in base_repo:
            results.append(Activity(
                fundraiser_id=fundraiser_id,
                distance=distance,
                activity_type=activity_type,
                date_start=date_start.strftime("%Y-%m-%d %H:%M:%S"),
                created_at=created_at.strftime("%Y-%m-%d %H:%M:%S")
            ))
        return results
