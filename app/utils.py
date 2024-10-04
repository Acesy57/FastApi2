from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")
def hash(hashed_password: str):
    return pwd_context.hash(hashed_password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)