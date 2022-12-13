import rsa
import hashlib
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import BLAKE2b


class Asymetric_Crypto:

    def __init__(self, content: str, public_key: str, crypto_algorithm: str):
        self.content = content.encode("utf-8")
        self.crypto_algorithm = crypto_algorithm
        self.public_key = public_key

    def get_signature(self, private_key):
        signer = PKCS115_SigScheme(private_key)
        return signer.sign(self.content)

    def get_content(self):
        return self.content.decode("utf-8")

    def encrypt(self):
        try:
            hash = BLAKE2b.new()
            hash.update(self.content)
            self.content = hash
        except Exception as exception:
            print(exception)

    def decrypt(self, private_key):
        try:
            self.content = rsa.decrypt(self.content, private_key)
        except Exception as exception:
            print(exception)
            return False

    def verify_signature(self, private_key):
        try:
            check = PKCS115_SigScheme(private_key).verify(self.content, self.get_signature(private_key))
            return check
        except Exception as exception:
            print(exception)
            return False
