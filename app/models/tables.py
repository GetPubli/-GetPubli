from app import db


class User(db.Model):
    __tablename__ = "users"


    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,  unique=True)
    password = db.Column(db.String)
    name     = db.Column(db.String)
    email    = db.Column(db.String)


    #O que vamos receber quando a classe for inicializada
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name     = name
        self.email    = email

    def __repr__(self):
        return "<User %r>" % self.username

class Funcionario(db.Model):
    __tablename__ = "funcionarios"


    id       = db.Column(db.Integer, primary_key=True)
    cpf      = db.Column(db.String,  unique=True)
    nome     = db.Column(db.String)
    cargo    = db.Column(db.String)


    def __init__(self, cpf, nome, cargo):
        self.cpf      = cpf
        self.nome     = nome
        self.cargo    = cargo

    def __repr__(self):
        return "<User %r>" % self.nome

