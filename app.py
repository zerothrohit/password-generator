from urllib import request
from flask import Flask, redirect, render_template, url_for, session

#import random
import secrets
import string


app = Flask(__name__, static_url_path='/static')
app.secret_key = "846446543"

@app.route('/', methods = ['GET', 'POST'])
def password_generator():
    # dictionary = ["alpha", "beta", "gamma", "delta"]
    # #print(random.choice(dictionary))
    # temp_pass = random.choice(dictionary)
    alphabet = string.ascii_letters + string.digits
    n = 10
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))

        if (any(c.islower() for c in password) and any(c.isupper()
        for c in password) and sum(c.isdigit() for c in password) >= 3):
            #print(password)
            break

    return render_template('index.html', password = password)


@app.route('/')
def refresh_password():
    return redirect(url_for('password_generator'))

if __name__ == "__main__":
    app.run(debug=True) 