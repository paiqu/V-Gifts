from werkzeug.exceptions import HTTPException

class InvalidToken(HTTPException):
    code = 400
    message = 'Invalid token!'

class InvalidUsername(HTTPException):
    code = 401
    message = 'Incorrect syntax! You can only use number, letter and underline.'

class InvalidEmail(HTTPException):
    code = 402
    message = 'Incorrect email format! Please try again.'

class UsernameAlreadyExit(HTTPException):
    code = 403
    message = 'Name is already exist! Please try another one.'

class IncorrectUsername(HTTPException):
    code = 404
    message = 'Incorrect user name! Please try again.'

class InvalidPassword(HTTPException):
    code = 405
    message = 'Login fail! Invalid password or name! Please try again.'

class NotEoughFund(HTTPException):
    code = 406
    message = 'Not enough fund, purchase fail!'

class EmailAlreadyExit(HTTPException):
    code = 408
    message = 'Email already used by another account, try another one.'