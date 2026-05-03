import os

class DatabaseHandler:
    def __init__(self, password):
        # BUG: Storing password in plain text
        self.password = password
        print(f"Connected with password: {password}")  # SECURITY: Password in logs
    
    def execute_query(self, user_input):
        # SECURITY: SQL Injection - no parameterization
        query = f"DELETE FROM users WHERE name = '{user_input}'"
        return query
    
    def read_config(self):
        # BUG: No error handling for missing file
        config = open('config.txt', 'r')
        data = config.read()
        # BUG: File handle not closed
        return data

def calculate_total(prices):
    # BUG: No validation for empty list or non-numeric values
    total = 0
    for price in prices:
        total = total + price  # PERFORMANCE: Could use sum()
    return total

def get_user_age(user_dict):
    # BUG: No key existence check
    age = user_dict['age']
    return age

# SECURITY: Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
DATABASE_URL = "postgresql://admin:password123@localhost/db"
