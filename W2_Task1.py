users=[
    {"id":1,"name":"Alice","email":"alice@example.com"},
    {"id":2,"name":"Bob","email":"bob@example.com"},
]

#Add
def add_user(user):
    users.append(user)

#Read
def get_user_by_id(user_id):
    return next((user for user in users if user["id"] == user_id), None)

#update
def update_user(user_id, name=None, email=None):
    user = get_user_by_id(user_id)
    if user:
        if name:
            user["name"] = name
        if email:
            user["email"] = email
        return True
    return False

#delete
def delete_user(user_list, user_id):
    for user in user_list:
        if user['id'] == user_id:
            user_list.remove(user)
            print(f"User with id {user_id} deleted successfully.")
            return True
    print(f"User with id {user_id} not found.")
    return False

add_user({"id": 3, "name": "Charlie", "email": "charlie@example.com"})
print("After adding: " ,users)
print("Reading the id: ",get_user_by_id(2))
update_user(2, name="Bobby")
print("After updating: ",users)
delete_user(users, 1)  
print("After Deleting:" ,users)