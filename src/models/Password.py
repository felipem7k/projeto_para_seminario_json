import hashlib

class Password:
    def __init__(self, password: str):
        self.hash = password
    
    
    def equals(self, password: str) -> bool:
        return self.to_hash(password) == self.hash

    @staticmethod
    def to_hash(password: str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()