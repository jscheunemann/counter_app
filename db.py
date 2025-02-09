api_keys = {
    "e54d4431-5dab-474e-b71a-0db1fcb9e659": "7oDYjo3d9r58EJKYi5x4E8",
    "5f0c7127-3be9-4488-b801-c7b6415b45e9": "mUP7PpTHmFAkxcQLWKMY8t",
    "526508ec-41d3-4030-aceb-e07837f61b67": "aW8JsvYEAXmYBbaaERcB3m"
}

users = {
    "7oDYjo3d9r58EJKYi5x4E8": {
        "name": "Bob"
    },
    "mUP7PpTHmFAkxcQLWKMY8t": {
        "name": "Alice"
    },
    "aW8JsvYEAXmYBbaaERcB3m": {
        "name": "Jason"
    }
}

def check_api_key(api_key: str, api_secret: str):
    return api_key in api_keys and api_keys[api_key] == api_secret

def get_user_from_api_key(api_key: str):
    return users[api_keys[api_key]]
