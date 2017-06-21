from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql9179563:8MzV9iqH1H@sql9.freemysqlhosting.net/sql9179563'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign')
def sign():
    return render_template('sign.html')


@app.route('/process',methods = ['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    return render_template('index.html',name = name, comment = comment)

@app.route('/home',methods = ['GET','POST'])
def home():
    links = ['http://www.youtube.com','https://www.bing.com','https://www.python.org','https://www.enkato.com']
    return render_template('example.html',links=links)




if __name__ == '__main__':
    app.run(debug=True)
