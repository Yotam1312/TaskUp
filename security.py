from cryptography.fernet import Fernet
import os

FERNET_KEY = os.getenv("FERNET_KEY")

if not FERNET_KEY:
    raise ValueError("FERNET_KEY is not set! Add it to your .env file.")

fernet = Fernet(FERNET_KEY.encode())


def encrypt_password(password: str) -> str:
    """Encrypt a password using Fernet."""
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password: str) -> str:
    """Decrypt a password using Fernet."""
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()