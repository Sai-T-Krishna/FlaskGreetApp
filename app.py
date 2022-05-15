
from flask import Flask, render_template, request, flash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'saikrishna'

@app.route('/')
def home():
    flash("Hey! What's your name")
    return render_template('index.html')

@app.route('/greet', methods = ['POST','GET'])
def greet():
    flash('Hi ' + str(request.form['name_input']) + ", Great to see you!")
    flash('Thank you for visiting')      
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug = True)