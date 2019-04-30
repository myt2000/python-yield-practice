import secrets

def secret_confirmation():
    a = secrets.SystemRandom()
    print(a)
    b = secrets.token_hex(256)
    print(b)

if __name__ == "__main__":
    secret_confirmation()