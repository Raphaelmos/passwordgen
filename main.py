import argparse
import random
import string
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def generate_password(length=12):
    local_random = random.SystemRandom()
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    password = [
        local_random.choice(lowercase),
        local_random.choice(uppercase),
        local_random.choice(digits),
        local_random.choice(special)
    ]

    remaining_length = length - len(password)
    all_chars = lowercase + uppercase + digits + special
    password += [local_random.choice(all_chars) for _ in range(remaining_length)]
    local_random.shuffle(password)
    return ''.join(password)

def main():
    parser = argparse.ArgumentParser(description="Generation of random passwords.")
    parser.add_argument('--length', type=int, default=12, help='Password length')
    parser.add_argument('--number', type=int, default=5, help='Number of passwords to generate')
    parser.add_argument('--output', type=str, default='passwords.txt', help='File for saving passwords')
    parser.add_argument('--workers', type=int, default=4, help='Number of threads for generation')
    args = parser.parse_args()

    with open(args.output, 'w', buffering=1) as file:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = [executor.submit(generate_password, args.length) for _ in range(args.number)]
            for future in tqdm(as_completed(futures), total=args.number, desc="Generating passwords"):
                password = future.result()
                file.write(password + '\n\n')
                file.flush()

    print(f"\nAll passwords are saved in the file: {args.output}")

if __name__ == "__main__":
    main()
