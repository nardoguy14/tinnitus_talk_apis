from domain.user import User, UserSearch
import mysql.connector
from repository.base_repository import BaseRepository


def update_user(user_claims, user: User):
    with BaseRepository() as base_repo:
        params = []

        if user.firstName:
            params.append(' first_name = %s ')
        if user.lastName:
            params.append(' last_name = %s ')
        if user.description:
            params.append(' description = %s ')
        if user.email:
            params.append(' email = %s ')
        if user.password:
            params.append(' password = %s ')
        if user.dateOfBirth:
            params.append(' dateOfBirth = %s ')
        if user.streetAddress1:
            params.append(' streetAddress1 = %s ')
        if user.streetAddress2:
            params.append(' streetAddress2 = %s ')
        if user.country:
            params.append(' country = %s ')
        if user.zipCode:
            params.append(' zip = %s ')
        if user.phoneNumber:
            params.append(' phoneNumber = %s ')

        query_str = f" , ".join(params)

        params = [user.firstName, user.lastName, user.description, user.email,
                  user.password, user.dateOfBirth, user.streetAddress1, user.streetAddress2,
                  user.country, user.zipCode, user.phoneNumber, user_claims['username']]
        filtered_params = tuple(list(filter(lambda x: x != None, params)))

        sql = f"""
        UPDATE users 
        SET
        {query_str}
        WHERE username = %s"""

        base_repo.execute(sql, filtered_params)
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
