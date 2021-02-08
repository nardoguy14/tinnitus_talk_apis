import bcrypt


def check_password(password: str, hash):
    return bcrypt.checkpw(password.encode('utf-8'), hash)

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')