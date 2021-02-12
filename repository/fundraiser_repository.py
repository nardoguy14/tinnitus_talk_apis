from typing import Optional
from domain.fundraisers import Fundraiser
import mysql.connector


def create_fundraiser(fundraiser: Fundraiser):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )

    cursor = mydb.cursor()
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

    cursor.execute(sql, val)
    mydb.commit()

    cursor.close()
    mydb.close()
    return {"result": "saved"}

def update_fundraiser(fundraiser: Fundraiser):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )
    cursor = mydb.cursor()
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
    cursor.execute(sql, val)
    mydb.commit()

    cursor.close()
    mydb.close()
    return {"result": "updated"}


def get_fundraisers(name: Optional[str], id: Optional[int]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )
    cursor = mydb.cursor()

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
    cursor.execute(query, filtered_params)

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
         date_end) in cursor:
        print(date_start)
        print(type(date_start))
        results.append(Fundraiser(id=id, name=name, description=description,
                                address=address, city=city, state=state, zip=zip,
                                date_start=date_start.strftime("%Y-%m-%d %H:%M:%S"),
                                date_end=date_end.strftime("%Y-%m-%d %H:%M:%S")))

    cursor.close()
    mydb.close()
    return results
