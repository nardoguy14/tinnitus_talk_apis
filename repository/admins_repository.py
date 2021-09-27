from typing import List, Optional
from domain.user import User, UserSearch
import mysql.connector
from domain.admin import Schedule
from repository.base_repository import BaseRepository


def update_schedule(schedule: Schedule):
    with BaseRepository() as base_repo:
        params = []

        if schedule.date:
            params.append(' date = %s ')
        if schedule.start_time:
            params.append(' start_time = %s ')
        if schedule.end_time:
            params.append(' end_time = %s ')

        query_str = f" , ".join(params)

        params = [schedule.date, schedule.start_time, schedule.end_time, schedule.id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))

        sql = f"""
        UPDATE schedules 
        SET
        {query_str}
        WHERE id = %s"""

        base_repo.execute(sql, filtered_params)
        return {"result": "updated"}


def create_schedule(schedule: Schedule):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO schedules (
        admin_id, date, start_time, end_time
        ) VALUES (%s, %s, %s, %s)"""
        val = (schedule.admin_id, schedule.date, schedule.start_time, schedule.end_time)
        base_repo.execute(sql, val)
        schedule.id = base_repo.lastrowid
        return schedule


def get_schedule(id: Optional[int]) -> List[Schedule]:
    with BaseRepository() as base_repo:

        query_params = []
        if id:
            query_params.append(" id = %s")

        query_str = " AND ".join(query_params)

        query = ("""SELECT
                        id, 
                        admin_id,
                        date,
                        start_time,
                        end_time,
                        created_at,
                        modified_at
                    FROM schedules
                """
                 f"WHERE {query_str}"
                 )

        params = [id]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))

        base_repo.execute(query, filtered_params)

        results = []
        for (id, admin_id, date, start_time, end_time, created_at, modified_at) in base_repo:
            print(date)
            results.append(Schedule(id=id,
                                    admin_id=admin_id,
                                    date=str(date),
                                    start_time=str(start_time),
                                    end_time=str(end_time),
                                    created_at=str(created_at),
                                    modified_at=str(modified_at)
                                ))
        return results


def get_schedules() -> List[Schedule]:
    with BaseRepository() as base_repo:
        query = ("""SELECT
                        id, 
                        admin_id,
                        date,
                        start_time,
                        end_time,
                        created_at,
                        modified_at
                    FROM schedules
                """
                 )

        base_repo.execute(query)

        results = []
        for (id, admin_id, date, start_time, end_time, created_at, modified_at) in base_repo:
            print(date)
            results.append(Schedule(id=id,
                                    admin_id=admin_id,
                                    date=str(date),
                                    start_time=str(start_time),
                                    end_time=str(end_time),
                                    created_at=str(created_at),
                                    modified_at=str(modified_at)
                                    ))
        return results

