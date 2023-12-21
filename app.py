from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/registration',methods=['GET', 'POST'])
def registration():
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(debug=True)
