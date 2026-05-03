import json
import pickle

def load_user_data(filename):
    # BUG: Using pickle without validation - security risk
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

def authenticate_user(username, password):
    # SECURITY: Hardcoded credentials
    if username == "admin" and password == "admin123":
        return True
    return False

def process_payment(amount, card_number):
    # SECURITY: No input validation for card number
    # BUG: Using float for money calculations
    fee = amount * 0.029
    total = amount + fee
    print(f"Processing ${total} on card {card_number}")
    return total

def fetch_data(url):
    # BUG: No error handling for network requests
    import requests
    response = requests.get(url)
    # BUG: No status code check
    return response.json()

def save_config(config_dict, filename='config.json'):
    # BUG: Mutable default argument
    config_dict['timestamp'] = 'now'
    with open(filename, 'w') as f:
        json.dump(config_dict, f)

class UserSession:
    sessions = []  # BUG: Class variable shared across instances
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.sessions.append(user_id)
    
    def get_user_info(self, user_id):
        # SECURITY: SQL injection
        query = f"SELECT * FROM users WHERE id = {user_id}"
        return query

def merge_dicts(dict1, dict2):
    # PERFORMANCE: Inefficient dictionary merging
    result = {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        result[key] = dict2[key]
    return result

# SECURITY: API keys exposed
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DATABASE_PASSWORD = "SuperSecret123!"
