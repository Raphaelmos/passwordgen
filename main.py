import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    remaining_length = length - len(password)
    all_chars = lowercase + uppercase + digits + special
    
    for _ in range(remaining_length):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)
    return ''.join(password)
def main():
    while True:
        password = generate_password()
        print(f"\nGenerated Password: {password}")
        
        choice = input("\nNot Satisfied ? Generate another password (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()
