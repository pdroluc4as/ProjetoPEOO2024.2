import json
from models.CRUD import CRUD

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"id: {self.id}, nome: {self.nome}, email: {self.email}, senha: {self.senha}"
    



class Usuarios(CRUD):
    @classmethod
    def salvar(cls):
        with open("usuarios.json", mode="w") as arquivo:   
            json.dump(cls.objetos, arquivo, indent = 4, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("usuarios.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj["id"], obj["nome"], obj["email"], obj["senha"])
                cls.objetos.append(c)
        except FileNotFoundError:
            pass