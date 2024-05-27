from app import app
from flask import render_template


@app.route('/index.html')
@app.route('/')
def index():
     return render_template('index.html')

@app.route('/k1.html')
def k1():
    return render_template('k1.html')

@app.route('/k2.html')
def k2():
    return render_template('k2.html')

@app.route('/k3.html')
def k3():
    return render_template('k3.html')

@app.route('/k4.html')
def k4():
    return render_template('k4.html')

@app.route('/k5.html')
def k5():
    return render_template('k5.html')

@app.route('/k6.html')
def k6():
    return render_template('k6.html')

@app.route('/k7.html')
def k7():
    return render_template('k7.html')

@app.route('/k8.html')
def k8():
    return render_template('k8.html')

@app.route('/k9.html')
def k9():
    return render_template('k9.html')

@app.route('/k10.html')
def k10():
    return render_template('k10.html')

@app.route('/k11.html')
def k11():
    return render_template('k11.html')

@app.route('/k12.html')
def k12():
    return render_template('k12.html')
