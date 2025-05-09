import hashlib

# Dictionary to store username and hashed password
users = {}

#  register a new user
def register(username, password):
    if username in users:
        print("User already exists.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        print("Created new user")

# login
def login(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username] == hashed_password:
        print("Login Successful")
    else:
        print("Invalid username or password")

register("john", "mypassword")   
login("john", "mypassword")      
