import re

TOKEN_REGEX = r'^[A-Za-z0-9\-._~]{20,80}$'

def is_valid_token(token: str) -> bool:
    return re.match(TOKEN_REGEX, token) is not None 