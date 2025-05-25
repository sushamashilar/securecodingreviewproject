import os
import subprocess

def login(username, password):
    stored_username = os.getenv("APP_USERNAME")
    stored_password = os.getenv("APP_PASSWORD")

    if not stored_username or not stored_password:
        print("Environment variables for credentials are not set.")
        return

    if username == stored_username and password == stored_password:
        print("Login successful!")
    else:
        print("Invalid credentials.")

def get_file_contents(filename):
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    
    try:
        with open(filename, 'r') as file:
            print(f"Contents of {filename}:")
            print(file.read())
    except Exception as e:
        print(f"Error reading file: {e}")

def secure_subprocess():
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(["cmd", "/c", "dir"], check=True)
        else:  # Unix-based systems
            subprocess.run(["ls", "-l"], check=True)
    except Exception as e:
        print(f"Command execution failed: {e}")

# Test the functions
login("admin", "password123")
get_file_contents("testfile.txt")
secure_subprocess()