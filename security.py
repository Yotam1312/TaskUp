from cryptography.fernet import Fernet
import os

# Fernet key - generate once and keep secure
# Generate with: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
FERNET_KEY = os.getenv("FERNET_KEY", "Xs3bvKAoh1A2VNSeicogTcpUX4gbSzyAWLoh5scm6B4=")

fernet = Fernet(FERNET_KEY.encode())


def encrypt_password(password: str) -> str:
    """Encrypt a password using Fernet."""
    encrypted = fernet.encrypt(password.encode())
    return encrypted.decode()


def decrypt_password(encrypted_password: str) -> str:
    """Decrypt a password using Fernet."""
    decrypted = fernet.decrypt(encrypted_password.encode())
    return decrypted.decode()
