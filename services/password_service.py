import bcrypt


def check_password(password: str, hash: str):
    return bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8'))

def hash_password(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(12)).decode('utf-8')