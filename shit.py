import bcrypt


def hash_password(password):
    # Generate a salt and hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed_password.decode('utf-8')


def verify_password(plain_password, hashed_password):
    # Check if the plain password matches the hashed password
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


# Example usage:
original_password = "my_secure_password"
hashed_password = hash_password(original_password)

# Simulate a login attempt
entered_password = "my_secure_password"
if verify_password(entered_password, hashed_password):
    print("Login successful!")
else:
    print("Login failed. Incorrect password.")
