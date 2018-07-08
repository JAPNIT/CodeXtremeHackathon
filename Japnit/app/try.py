from flask import Flask,render_template, url_for, redirect , request
import os.path, sqlite3

app = Flask(__name__)

def get_db():
    db = sqlite3.connect('db.sqlite3')
    print("opened db")
    db.row_factory = sqlite3.Row
    return db

def create_db():
    db = get_db()
    db.execute('CREATE TABLE posting (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT)')
    print("created")
    db.close()

if not os.path.isfile('db.sqlite3'):
    create_db()

@app.route('/')
def index():
    return render_template('try.html')

@app.route('/aboutus/<n>')
def aboutus(n):
    return render_template('about.html',age = n)

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/student')
def student():
    return render_template('student.html')
"""
@app.route('/form/', methods=['GET','POST'])

def form():
    if request.method == 'POST':
        return render_template('result.html', username = request.form['username'])
    else:
        return render_template('form.html')
"""
@app.route('/form/', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        db = get_db()
        db.execute('INSERT INTO posting (username) VALUES (?)', (request.form['username'],) )
        db.commit()
        db.close()
        return redirect(url_for('success'))
    else:
        return render_template('form.html')

@app.route('/success/')
def success():
    db = get_db()
    records = db.execute('SELECT * FROM posting').fetchall()
    db.close()
    return render_template('db.html',records=records)

@app.route('/try/<x>')
def display(x):
    if x == "teacher":
        return redirect(url_for('teacher'))
    elif x == "student":
        return redirect(url_for('student')) 
    else:
        return 'enter valid'
if __name__ == '__main__':
    app.run(debug=True)




