from domain.user import User, UserSearch
import mysql.connector


def update_user(user: User):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )
    cursor = mydb.cursor()
    sql = """UPDATE users 
    SET
    first_name = %s,
    last_name  = %s,
    email = %s,
    description = %s,
    password = %s
    WHERE username = %s"""
    val = (user.first_name, user.last_name, user.email,
           user.description, user.password,user.username)
    cursor.execute(sql, val)
    mydb.commit()

    cursor.close()
    mydb.close()
    return {"result": "updated"}

def create_user(user: User):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )

    cursor = mydb.cursor()
    sql = """INSERT INTO users (
    username,
    first_name,
    last_name,
    email,
    description,
    password
    ) VALUES (%s, %s, %s, %s, %s, %s)"""
    val = (user.username, user.first_name, user.last_name,
           user.email, user.description, user.password)
    cursor.execute(sql, val)
    mydb.commit()

    cursor.close()
    mydb.close()
    return {"result": "saved"}

def get_user(user_search: UserSearch):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="CAMera14",
        database="tinnitus_talks"
    )
    cursor = mydb.cursor()

    query_params = []
    if user_search.first_name:
        query_params.append(" first_name = %s ")
    if user_search.last_name:
        query_params.append(" last_name = %s ")
    if user_search.username:
        query_params.append(" username = %s ")
    if user_search.email:
        query_params.append(" email = %s ")

    query_str = " AND ".join(query_params)

    query = ("SELECT username, first_name, last_name, email, description FROM users "
             f"WHERE {query_str}")

    params = [user_search.first_name, user_search.last_name,
              user_search.username, user_search.email]
    filtered_params = tuple(list(filter(lambda x: x != None, params)))

    cursor.execute(query, filtered_params)

    results = []
    for (username, first_name, last_name, email, description) in cursor:
        results.append(User(username=username, first_name=first_name,
                            last_name=last_name, description=description,
                            email=email))

    cursor.close()
    mydb.close()
    return results
