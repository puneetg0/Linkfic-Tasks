START

INPUT email, password

SEARCH database for user by email

IF user does not exist:
    RETURN "Invalid credentials"

IF password does not match stored hash:
    RETURN "Invalid credentials"

GENERATE JWT with user ID and expiry

RETURN JWT token

END