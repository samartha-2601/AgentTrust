import base64

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15


def sign_message(message: str, private_key: str):

    key = RSA.import_key(private_key)

    message_hash = SHA256.new(message.encode())

    signature = pkcs1_15.new(key).sign(message_hash)

    return base64.b64encode(signature).decode()


def verify_message(
    message: str,
    signature: str,
    public_key: str
):

    try:

        key = RSA.import_key(public_key)

        message_hash = SHA256.new(message.encode())

        decoded_signature = base64.b64decode(signature)

        pkcs1_15.new(key).verify(
            message_hash,
            decoded_signature
        )

        return True

    except Exception:

        return False