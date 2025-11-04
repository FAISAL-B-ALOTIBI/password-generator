import secrets
import string

def generate_password(words=4, length=4):
    characters = string.ascii_lowercase + string.digits
    parts = []
    for _ in range(words):
        part = ''.join(secrets.choice(characters) for _ in range(length))
        parts.append(part)
    return '-'.join(parts)

print("Generated password:", generate_password())