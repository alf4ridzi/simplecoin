import hashlib
import base58

def hash_password_md5(password):
    hashed = hashlib.md5(password.encode('utf-8')).hexdigest()

    return hashed

def hash_sha256(content) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def create_wallet_number(username):
    # encrypt with sha256 first
    sha256 = hash_sha256(username)
    # encrypt with hash160
    simplecoin_address = base58.b58encode(sha256[:20]).decode('utf-8')

    return "0x" + simplecoin_address
