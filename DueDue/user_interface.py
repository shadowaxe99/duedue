```python
import os
from getpass import getpass

# Shared dependencies
supported_formats = ["XML", "JSON", "Markdown"]
user_config = {}
cloud_services = ["Google Drive", "Dropbox", "OneDrive"]
platforms = ["Windows", "macOS", "Linux"]
authentication_status = False

def display_menu():
    print("\nWelcome to DueDue!")
    print("1. Configure settings")
    print("2. View supported file formats")
    print("3. View supported cloud services")
    print("4. View supported platforms")
    print("5. Authenticate user")
    print("6. Exit")

def configure_settings():
    print("\nConfigure Settings:")
    user_config["notification"] = input("Enable notifications (yes/no): ")
    user_config["reminder"] = input("Set reminder (in days): ")
    user_config["cloud_service"] = input("Choose cloud service (Google Drive/Dropbox/OneDrive): ")
    user_config["platform"] = input("Choose platform (Windows/macOS/Linux): ")

def view_supported_formats():
    print("\nSupported File Formats:")
    for format in supported_formats:
        print(format)

def view_supported_cloud_services():
    print("\nSupported Cloud Services:")
    for service in cloud_services:
        print(service)

def view_supported_platforms():
    print("\nSupported Platforms:")
    for platform in platforms:
        print(platform)

def authenticate_user():
    global authentication_status
    username = input("\nEnter username: ")
    password = getpass("Enter password: ")
    # Call the authenticate_user function from authentication.py
    # authentication_status = authenticate_user(username, password)
    # For now, we'll just simulate successful authentication
    authentication_status = True
    print("Authentication successful!" if authentication_status else "Authentication failed!")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            configure_settings()
        elif choice == "2":
            view_supported_formats()
        elif choice == "3":
            view_supported_cloud_services()
        elif choice == "4":
            view_supported_platforms()
        elif choice == "5":
            authenticate_user()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```