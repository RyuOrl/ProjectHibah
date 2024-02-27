from flask import Flask, render_template, request
#cara run : python -m flask run

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
  return render_template('login.html')


@app.route('/login', methods=["POST"])
def post_login():
  nama = request.form.get('nama')
  nomor = request.form.get('nomor')
  return render_template('index.html', nama=nama, nomor=nomor)