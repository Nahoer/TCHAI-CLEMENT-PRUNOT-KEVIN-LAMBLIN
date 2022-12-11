import rsa
class Asymetric_Crypto:

    def __init__(self, content:str, public_key:str, crypto_algorithm:str):
        self.content = content.encode("utf-8")
        self.crypto_algorithm = crypto_algorithm
        self.public_key = public_key

    def get_signature(self, private_key):
        return rsa.sign(self.content, private_key, self.crypto_algorithm)
    def get_content(self):
        return self.content.decode("utf-8")

    def encrypt(self):
        self.content = rsa.encrypt(self.content, self.public_key)

    def decrypt(self, private_key):
        try:
            self.content = rsa.decrypt(self.content, private_key)
        except:
            return False
    def verify_signature(self, private_key):
        try: return rsa.verify(self.content, self.get_signature(private_key), private_key) == self.crypto_algorithm
        except: return False




