import hashlib

def hash_sha256(content) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def hash_md5(content) -> str:
    return hashlib.md5(content.encode('utf-8')).hexdigest()