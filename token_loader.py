TOKEN_FILENAME = "token.txt"


def load_token(filename=TOKEN_FILENAME):
    with open(filename, 'r', newline='\n') as token_file:
        token = token_file.readline()
        return token
