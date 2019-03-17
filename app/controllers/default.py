from flask import render_template
from flask import jsonify
from flask import request
from flask import make_response
from flask import abort
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from app import app, db
import requests as req
import json
import urllib.request
import requests
import urllib

from app.models.tables import User, Funcionario
from app.models.forms import LoginForm


@app.route("/", methods=["GET", "POST"])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		f = form.url.data
		v = form.file.data
		urllib.request.urlretrieve(f,v)
	return render_template('jpg.html', form = form)




@app.route("/zip", methods=["GET", "POST"])
def zip():
	form = LoginForm()
	if form.validate_on_submit():
		f = form.url.data
		v = form.file.data
		r = requests.get(f)
		
		with open(v, "wb") as code:
			code.write(r.content)

	return render_template('zip.html', form = form)




@app.route("/pdf", methods=["GET", "POST"])
def pdf():
	form = LoginForm()
	if form.validate_on_submit():
		f = form.url.data
		v = form.file.data
		r = requests.get(f)
		
		with open(v, "wb") as code:
			code.write(r.content)

	return render_template('pdf.html', form = form)


@app.route("/get/funcionario/<info_get>", methods=["GET"])
def get(info_get):
		#execução do get no BD
		cpf = info_get
		r = Funcionario.query.filter_by(cpf=cpf).first()   #all()
		#resultado no cmd
		print(r)
		#resultado na aplicação
		resultado_nome  = r.nome
		resultado_cargo = r.cargo
		resultado_cpf   = r.cpf
		if resultado_nome and resultado_cargo and resultado_cpf:
			dados = {"Nome": resultado_nome, "Cargo": resultado_cargo, "CPF": resultado_cpf}
			return jsonify(dados), 200
		else:
			dados = ({"Status":"Erro"})
			return jsonify(dados), 404

@app.route("/delete/funcionario/<info_del>", methods=["GET","DELETE"])
def delete(info_del):
	#execução do delete no BD
	cpf = info_del
	r = Funcionario.query.filter_by(cpf=cpf).first()
	db.session.delete(r)
	db.session.commit()
	#resultado no CMD
	print(r)
	#resultado na aplicação
	resultado_nome  = r.nome
	resultado_cargo = r.cargo
	resultado_cpf   = r.cpf
	try:
		dados = {"Nome": resultado_nome, "Cargo": resultado_cargo, "CPF": resultado_cpf}
		return jsonify(dados), 200
	except:
		dados = ({"Status":"Erro"})
		return jsonify(dados), 404


@app.route("/post/funcionario/", methods=["GET", "POST"])
def post():
	if not request.json:
		return make_response(jsonify({'error': 'Format not json'}), 400)
	else:
		cpf   = request.json["cpf"]
		nome  = request.json["nome"]
		cargo = request.json["cargo"]
		i = Funcionario(cpf, nome, cargo)
		db.session.add(i)
		db.session.commit()
		#resultado no CMD
		print(i)
		#resultado na aplicação
		resultado_nome  = r.nome
		resultado_cargo = r.cargo
		resultado_cpf   = r.cpf
		try:
			dados = {"Nome": resultado_nome, "Cargo": resultado_cargo, "CPF": resultado_cpf}
			dados.append(dados)
			return jsonify(dados), 200
		except:
			dados = {"Status":"Erro"}
			return jsonify(dados), 404

#-------------------------------MENUS------------------------------------------------
@app.route("/get_menu", methods=["GET"])
def get_menu():
	#form = LoginForm()
	#if form.validate_on_submit():
	#	print(form.cpf.data)
	#	cpf = (form.cpf.data)
	#	r = Funcionario.query.filter_by(cpf=info_get).all()
	#	print(r)
	#	return "OK"
	#else:
	return render_template('get.html') #, form = form)

@app.route("/post_menu", methods=["GET"])
def post_menu():
	#form = LoginForm()
	#if form.validate_on_submit():
	#	print(form.cpf.data)
	#	cpf = (form.cpf.data)
	#	resultado = post(cpf)
	#	return "OK"
	return render_template('post.html') #, form = form)

@app.route("/delete_menu", methods=["GET"])
def delete_menu():
	#form = LoginForm()
	#if form.validate_on_submit():
	#	print(form.cpf.data)
	return render_template('delete.html') #, form = form)
#-------------------------------MENUS------------------------------------------------



@app.route("/base")
def BASE():
	return render_template('base.html')







