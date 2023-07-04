```python
import getpass

authentication_status = False

def authenticate_user():
    global authentication_status
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    # This is a placeholder for actual authentication logic
    # In a real-world application, you would not store passwords in plain text
    # You would likely use a database and a secure method of storing passwords
    if username == "admin" and password == "password":
        authentication_status = True
        print("Authentication successful.")
    else:
        print("Authentication failed.")

    return authentication_status
```