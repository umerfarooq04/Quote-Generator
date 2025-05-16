from flask import Flask, render_template, session, redirect, url_for
from utils import get_random_quote, save_to_history, load_history
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session

@app.route('/')
def index():
    quote, author = get_random_quote()
    session['current_quote'] = (quote, author)
    save_to_history(quote, author)
    return render_template("index.html", quote=quote, author=author)

@app.route('/like')
def like():
    if 'likes' not in session:
        session['likes'] = []
    quote, author = session.get('current_quote', ("", ""))
    session['likes'].append((quote, author))
    return redirect(url_for('index'))

@app.route('/history')
def history():
    past_quotes = load_history()
    return render_template("history.html", quotes=past_quotes)
