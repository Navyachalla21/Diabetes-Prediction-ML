from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import numpy as np
from prediction import predict_res

app = Flask(__name__)
app.secret_key = "diabetes"


@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["password"]
        r1 = pd.read_excel('user.xlsx')
        for index, row in r1.iterrows():
            if row["email"] == str(email) and row["password"] == str(pwd):
                return redirect(url_for('index'))
        else:
            msg = 'Invalid Login Try Again'
            return render_template('login.html', msg=msg)
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['Email']
        password = request.form['Password']
        col_list = ["name", "email", "password"]
        r1 = pd.read_excel('user.xlsx', usecols=col_list)
        new_row = {'name': name, 'email': email, 'password': password}
        r1 = r1.append(new_row, ignore_index=True)
        r1.to_excel('user.xlsx', index=False)
        print("Records created successfully")
        # msg = 'Entered Mail ID Already Existed'
        msg = 'Registration Successful !! U Can login Here !!!'
        return render_template('login.html', msg=msg)
    return render_template('register.html')


@app.route('/password', methods=['POST', 'GET'])
def password():
    if request.method == 'POST':
        current_pass = request.form['current']
        new_pass = request.form['new']
        verify_pass = request.form['verify']
        r1 = pd.read_excel('user.xlsx')
        for index, row in r1.iterrows():
            if row["password"] == str(current_pass):
                if new_pass == verify_pass:
                    r1.replace(to_replace=current_pass,
                               value=verify_pass, inplace=True)
                    r1.to_excel("user.xlsx", index=False)
                    msg1 = 'Password changed successfully'
                    return render_template('password_change.html', msg1=msg1)
                else:
                    msg2 = 'Re-entered password is not matched'
                    return render_template('password_change.html', msg2=msg2)
        else:
            msg3 = 'Incorrect password'
            return render_template('password_change.html', msg3=msg3)
    return render_template('password_change.html')


@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    return render_template("prediction.html")


@app.route('/graphs', methods=['POST', 'GET'])
def graphs():
    return render_template("graphs.html")


@app.route('/predict', methods=['POST'])
def predict():
    ui = []

    if request.method == 'POST':
        ui.append(int(request.form['q1']))
        ui.append(int(request.form['q2']))
        ui.append(int(request.form['q3']))
        ui.append(int(request.form['q4']))
        ui.append(int(request.form['q5']))
        ui.append(float(request.form['q6']))
        ui.append(float(request.form['q7']))
        ui.append(int(request.form['q8']))

    l = []
    for i in ui:
        l.append(i)
    l1 = []
    l1.append(l)
    print("l1", l1)
    p = predict_res(l1)
    print(p)

    class_name = p[0]
    class_label = p[1]

    return render_template('result.html', class_name=class_name, u=class_label)


@app.route('/logout')
def logout():
    session.clear()
    msg = 'You are now logged out'
    return redirect(url_for('login', msg=msg))


if __name__ == '__main__':
    app.run(port=5055, debug=True)
