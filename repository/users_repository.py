from domain.user import User
import mysql.connector
import bcrypt

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
