import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(username, password):
    """Save the password for the given username."""
    with open('passwords.txt', 'a') as f:
        f.write(f"{username}: {password}\n")

if __name__ == '__main__':
    username = input("Enter a username: ")
    password_length = int(input("Enter the desired length of the password: "))

    password = generate_password(password_length)
    save_password(username, password)

    print(f"Password saved for {username}!")
