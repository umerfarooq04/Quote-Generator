import random

def load_quotes(file_path="quotes.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def get_random_quote():
    quotes = load_quotes()
    return random.choice(quotes)

