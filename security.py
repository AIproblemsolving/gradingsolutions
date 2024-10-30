import hashlib

hashed_password = "b8ea7b7963a0fa7baaf4d71f4f0dc75a42aa7e4e1f3a406c809ca5b16ac7e9ab"
hashed_api_keys = [
    "e08238f0174d5c63c56780b1e0587fcb123f4d3441a9008c973e9177c1dffd97",
    "0d4ca4d734049d4c5f0cc6cb5928492a3ad85068de45e0cdbadefbe1af37545e",
    "b27e587b8a57fb8bbb8c57e51d229884366a14e29e54d64974871b4c13c4d810"
]

api_key_user = [
    "admin",
    "beta.user",
    "NewAPI.Test"
]

def hash_input(input_text):
    return hashlib.sha256(input_text.encode()).hexdigest()

def check_password(input_password):
    return hash_input(input_password) == hashed_password

def check_api_key(input_api_key):
    return hash_input(input_api_key) in hashed_api_keys

def api_key_index(input_api_key):
    hashed_input = hash_input(input_api_key)
    if hashed_input in hashed_api_keys:
        return hashed_api_keys.index(hashed_input)
    else:
        return None  # Return None if no match is found

def get_api_key_user(input_api_key):
    index = api_key_index(input_api_key)
    if index is not None and index < len(api_key_user):
        return api_key_user[index]
    else:
        return None  # Return None if the index is invalid
