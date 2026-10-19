print("hellow world")

users=[
    {
        "username": "ouma",
        "password": "Ous"
    }
]

students=["Hey", "Hi", "Hello"]
print(students)

def login(username, password):
    for user in users:
        if user['username'] == username.lower() and user['password'] == password:
            print("Logged in")