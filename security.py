import hashlib

hashed_password = "b8ea7b7963a0fa7baaf4d71f4f0dc75a42aa7e4e1f3a406c809ca5b16ac7e9ab"
hashed_api_keys = ["e08238f0174d5c63c56780b1e0587fcb123f4d3441a9008c973e9177c1dffd97",
                   "placeholder"]

def hash_input(input_text):
    return hashlib.sha256(input_text.encode()).hexdigest()

def check_password(input_password):
    return hash_input(input_password) == hashed_password

def check_api_key(input_api_key):
    return hash_input(input_api_key) in hashed_api_keys
