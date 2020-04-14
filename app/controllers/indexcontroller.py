from app import app
from flask import render_template
from app.models.user import User ## import kelas User dari model

@app.route('/', methods = ['GET'])
def index():
	user = User() ## membuat objek dari kelas user
	nama = user.getName() ## memanggil method untuk mengambil nama
	return render_template('index.html', nama=nama)