from domain.user import User, UserSearch
import mysql.connector
from repository.base_repository import BaseRepository


def update_user(user: User):
    with BaseRepository() as base_repo:
        sql = """UPDATE users 
        SET
        first_name = %s,
        last_name  = %s,
        email = %s,
        description = %s,
        password = %s,
        dateOfBirth = %s,
        streetAddress1 = %s,
        streetAddress2 = %s,
        country = %s,
        zip = %s,
        phoneNumber = %s
        WHERE username = %s"""
        val = (
               user.firstName, user.lastName, user.email,
               user.description, user.password,
               user.dateOfBirth, user.streetAddress1, user.streetAddress2,
               user.country, user.zipCode, user.phoneNumber, user.username
               )
        base_repo.execute(sql, val)
        return {"result": "updated"}


def create_user(user: User):
    with BaseRepository() as base_repo:
        sql = """INSERT INTO users (
        username,
        first_name,
        last_name,
        email,
        description,
        password,
        dateOfBirth,
        streetAddress1,
        streetAddress2,
        country,
        zip,
        phoneNumber
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (user.username, user.firstName, user.lastName,
               user.email, user.description, user.password,
               user.dateOfBirth, user.streetAddress1, user.streetAddress2,
               user.country, user.zipCode, user.phoneNumber)
        base_repo.execute(sql, val)
        return {"result": "saved"}


def get_user(user_search: UserSearch):
    with BaseRepository() as base_repo:

        query_params = []
        if user_search.user_id:
            query_params.append(" id = %s")
        if user_search.first_name:
            query_params.append(" first_name = %s ")
        if user_search.last_name:
            query_params.append(" last_name = %s ")
        if user_search.username:
            query_params.append(" username = %s ")
        if user_search.email:
            query_params.append(" email = %s ")

        query_str = " AND ".join(query_params)

        query = ("""SELECT
                        id, 
                        username, 
                        first_name, 
                        last_name, 
                        email, 
                        description 
                    FROM users """
                  f"WHERE {query_str}")

        params = [user_search.user_id, user_search.first_name, user_search.last_name,
                  user_search.username, user_search.email]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))

        base_repo.execute(query, filtered_params)

        results = []
        for (id, username, first_name, last_name, email, description) in base_repo:
            results.append(User(id=id,
                                username=username,
                                firstName=first_name,
                                lastName=last_name,
                                description=description,
                                email=email))
        return results


def get_password_hash(username: str):
    with BaseRepository() as base_repo:
        query = ("""SELECT 
                        password
                    FROM users
                    WHERE username = %s 
                """
                )

        params = [username]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))

        base_repo.execute(query, filtered_params)

        results = []
        for password in base_repo:
            results.append(password[0])

        print(results)
        return results
