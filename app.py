from tabnanny import check
from turtle import color
from unicodedata import digit
from flask import Flask, redirect, render_template, url_for, request

import random
import secrets
import string

app = Flask(__name__, static_url_path='/static')
app.secret_key = "846446543"

@app.route('/', methods = ['GET', 'POST'])
def password_generator():
    n = 12
    color = "green"
    strength = "Strong"
    characters = list(string.ascii_letters + string.digits + "@#!*-_"*random.randint(3,9))
    ascii = list(string.ascii_letters)
    digit = list(string.digits)
    symbol = list("@#!*-_"*random.randint(3,9))
    csl = css = csn = "checked"
    if request.method == 'POST':
        n = request.form['mynum']
        if int(n)<=10:
            color = "red"
            strength = "Weak"
        csl = css = csn = None
        mylist = request.form.getlist('mycheckbox')
        characters.clear()
        for i in mylist:
            if(i == 'letters') :
                csl = "checked"
                characters.extend(ascii)
            if(i == 'punctuation') :
                css = "checked"
                characters.extend(symbol)
            if(i == 'number') :
                csn = "checked"
                characters.extend(digit)
        if not mylist:
            return redirect(url_for('password_generator'))

    random.shuffle(characters)
    password = []
    for i in range(int(n)):
        password.append(secrets.choice(characters))
    random.shuffle(password)
    temp = "".join(password)

    return render_template('index.html', password = temp, num = n, checkl = csl, checks = css, checkn = csn, color = color, strength = strength)

@app.route('/')
def refresh_password():
    return redirect(url_for('password_generator'))

if __name__ == "__main__":
    app.run(debug=True) 