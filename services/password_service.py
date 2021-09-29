from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def check_hash_password(password,hashed_password):
    return pwd_context.verify(password,hashed_password)
def get_hash_password(password):
    return pwd_context.hash(password)


