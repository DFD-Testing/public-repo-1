import hashlib

# Function to generate MD5 hash
def generate_md5_hash(text):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the bytes-like object of the input string
    md5_hash.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    md5_hash_hex = md5_hash.hexdigest()

    return md5_hash_hex

# Example usage
password = input()
secure_hash = generate_md5_hash(password)
print("Secure Hash:",secure_hash)
