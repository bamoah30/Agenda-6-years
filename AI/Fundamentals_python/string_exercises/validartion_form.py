'''
This is a user validation program for only a particular entered data.
It checks if the entered data meets specific criteria.
Here are the criteria:
    Minimum 5 characters
    Maximum 10 characters
    Only lowercase letters
    Underscore and dot is allowed
    Whitespace, symbol are not allowed

'''
def validate_username(username):
    if len(username) < 5:
        return "Username must be at least 5 characters long."
    if len(username) > 10:
        return "Username must be at most 10 characters long."
    if not username.islower(): #This checks if all characters are lowercase if not it returns false
        return "Username must contain only lowercase letters."
    for char in username:
        if not (char.isalnum() or char in ['_', '.']):
            return "Username can only contain lowercase letters, digits, underscores, and dots."
    return "Valid username."