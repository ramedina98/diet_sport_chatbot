def process_input(user_input):
    """
    Processes user input: tokenizes, converts to lowercase and removes unwanted characters.
    """
    tokens = user_input.lower().split()
    return [token.strip(",.!?") for token in tokens]