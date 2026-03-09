# tests/test_validator.py

from app.validator import is_valid_token

def test_valid_token():
    token = "Abcdef12345-_~ABCDE1" 
    assert is_valid_token(token) == True

def test_invalid_token_short():
    token = "abc123"
    assert is_valid_token(token) == False

def test_invalid_token_chars():
    token = "Invalid$Token#1234567890"
    assert is_valid_token(token) == False