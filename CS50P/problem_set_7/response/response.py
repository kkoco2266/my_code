from validator_collection import validators, errors

email_address = input("What's your email address? ")
try:
    _ = validators.email(email_address)
    print('Valid')
except errors.EmptyValueError:
    print('Invalid')
except errors.InvalidEmailError:
    print('Invalid')
