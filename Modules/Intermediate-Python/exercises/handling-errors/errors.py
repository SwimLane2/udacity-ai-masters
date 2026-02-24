INVALID_PASSWORDS = (
    'password',
    'abc123',
    '123abc',
)


def validate_password(username, password):
    if password == username:
        raise InvalidPasswordError("Password cannot be the same as the username")
    
    if password in INVALID_PASSWORDS:
        raise InvalidPasswordError("That password is too common.")
    
    return True


def create_account(username, password):
    return (username, password)

class InvalidPasswordError(Exception):
    pass


def main(username, password):
    try:
        validate_password(username, password)
        account = create_account(username, password)
        print(account)
    except InvalidPasswordError as error:
        print(f"Oh no! {error}")


if __name__ == '__main__':
    main('jim', 'jam')
    main('admin', 'password')  # Oh no!
    main('guest', 'guest')  # Oh no!