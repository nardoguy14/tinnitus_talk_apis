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
