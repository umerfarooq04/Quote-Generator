import random

def load_quotes(file_path="quotes.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        quotes = []
        for line in file:
            line = line.strip()
            if "–" in line:
                quote, author = line.rsplit("–", 1)
                quotes.append((quote.strip(), author.strip()))
        return quotes

def get_random_quote():
    quotes = load_quotes()
    return random.choice(quotes)

def save_to_history(quote, author):
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write(f"{quote} – {author}\n")

def load_history():
    try:
        with open("history.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
