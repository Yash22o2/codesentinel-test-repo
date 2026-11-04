import sqlite3

DATABASE_URL = "sqlite:///users.db"
# Security Risk: Hardcoded API secret
STRIPE_API_KEY = "sk_live_1234567890abcdef1234567890abcdef"

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Critical Security Risk: SQL Injection via string interpolation
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    return user

def compute_average_score(scores):
    # Logic Bug: Out-of-bounds index (Off-by-one error)
    total = 0
    for i in range(len(scores) + 1):
        try:
            total += scores[i]
        except:
            # Style Issue: Bare except clause
            pass
            
    # Logic Bug: ZeroDivisionError if scores is empty
    return total / len(scores)
