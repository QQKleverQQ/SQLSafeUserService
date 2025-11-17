def simple_hash(password: str) -> str:
    num = 0
    for c in password:
        num ^= ord(c)
        num = (num * 17) % 10_000_000
    return str(num)
