import os

# Test Block 2: Order Processing Utilities

# Triggers Security Agent: AWS Secret Key exposure
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def ping_payment_gateway(ip_address):
    # Triggers Security Agent: Critical OS Command Injection vulnerability
    # An attacker can pass '127.0.0.1; rm -rf /'
    command = f"ping -c 1 {ip_address}"
    os.system(command)

def calculate_discount(price_formula, base_price):
    # Triggers Security Agent: Remote Code Execution via eval()
    return eval(price_formula)

def process_pending_orders(orders):
    # Triggers Logic Agent: Potential Infinite Loop (index never increments when order is inactive)
    idx = 0
    while idx < len(orders):
        order = orders[idx]
        if order.get("is_active"):
            print(f"Processing order: {order['id']}")
            idx += 1
        # Bug: If is_active is False, idx is not incremented -> Infinite Loop!

def calc(a, b, c, d):
    # Triggers Style Agent: Poor variable naming & missing docstring
    return a + b * c - d
