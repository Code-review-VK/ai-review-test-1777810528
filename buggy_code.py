def divide(a, b):
    # BUG: Missing error handling for division by zero
    return a / b

def calculate_average(numbers):
    # BUG: No check for empty list
    total = sum(numbers)
    return total / len(numbers)

def fetch_user_data(user_id):
    # SECURITY: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return execute_query(query)

def get_api_data(api_key):
    # SECURITY: API key exposed in URL
    import requests
    url = f"https://api.example.com/data?key={api_key}"
    response = requests.get(url)
    # BUG: No error handling for failed requests
    return response.json()

def process_file(filename):
    # BUG: No try-except for file operations
    file = open(filename, 'r')
    data = file.read()
    # BUG: File not closed - resource leak
    return data

def merge_lists(list1, list2):
    # PERFORMANCE: Inefficient O(n²) operation
    result = []
    for item in list1:
        if item not in result:
            result.append(item)
    for item in list2:
        if item not in result:
            result.append(item)
    return result

class UserManager:
    def __init__(self):
        # BUG: Mutable default argument
        self.users = []
    
    def add_user(self, user, permissions=[]):
        # BUG: Mutable default argument will cause issues
        permissions.append('read')
        user['permissions'] = permissions
        self.users.append(user)
