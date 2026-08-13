import hashlib
import os

# 1. STYLE: Missing docstring, bad spacing
def verify_user(username,password, db_hash):
    # 2. SECURITY: MD5 is cryptographically broken and should not be used for passwords
    current_hash = hashlib.md5(password.encode()).hexdigest()
    
    # 3. STYLE / LOGIC: Bad formatting, and vulnerable to timing attacks (should use hmac.compare_digest)
    if(current_hash==db_hash): return True
    else: return False

def get_api_key():
    # 4. SECURITY: Hardcoded sensitive credentials in source code
    secret_key = "sk_live_12345ABCDE"
    return secret_key

class MathHelper:
    # 5. LOGIC: Potential ZeroDivisionError is not handled
    def divide_numbers(self, a, b):
        return a / b
