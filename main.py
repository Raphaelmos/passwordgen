import random
import string
import argparse

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
    parser = argparse.ArgumentParser(description="Generate random passwords.")
    parser.add_argument('--length', type=int, default=12, help='Length of each password')
    parser.add_argument('--number', type=int, default=5, help='Number of passwords to generate')
    parser.add_argument('--output', type=str, default='passwords.txt', help='Output file to save passwords')

    args = parser.parse_args()

    passwords = []
    for _ in range(args.number):
        password = generate_password(args.length)
        passwords.append(password)
        print(f"\nGenerated Password: {password}")

    with open(args.output, 'w') as file:
        for password in passwords:
            file.write(password + '\n\n')

    print(f"\nAll passwords have been saved to {args.output}")

if __name__ == "__main__":
    main()
