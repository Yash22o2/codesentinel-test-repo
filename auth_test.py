import sqlite3

# Dummy code with intentional flaws to trigger all 4 CodeSentinel agents

DATABASE_URL = "sqlite:///users.db"
# Triggers Security Agent: Hardcoded API secret
STRIPE_API_KEY = "sk_live_1234567890abcdef1234567890abcdef"

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Triggers Security Agent: SQL Injection vulnerability (string interpolation)
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    
    return user

def compute_average_score(scores):
    # Triggers Logic Agent: Out-of-bounds index + Division by zero risk
    total = 0
    for i in range(len(scores) + 1):  # Off-by-one bug
        try:
            total += scores[i]
        except:  # Triggers Style Agent: Bare except clause without specific exception
            pass
            
    # Logic Agent: Unhandled ZeroDivisionError if scores is empty
    return total / len(scores)
