import hashlib

md5_hash = hashlib.md5()
a_file = open("url.py", "rb")
content = a_file.read()
md5_hash. update(content)
digest = md5_hash.hexdigest()
print(digest)