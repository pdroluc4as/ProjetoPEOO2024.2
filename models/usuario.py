import json
from models.CRUD import CRUD

class Usuario:
    def __init__(self, id, nome, email, senha, vendedor):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__vendedor = vendedor

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def senha(self):
        return self.__senha

    @property
    def vendedor(self):
        return self.__vendedor

    # Setters
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @email.setter
    def email(self, novo_email):
        self.__email = novo_email

    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha

    @vendedor.setter
    def vendedor(self, novo_vendedor):
        self.__vendedor = novo_vendedor

    def __str__(self):
        return f"id: {self.__id}, nome: {self.__nome}, email: {self.__email}, senha: {self.__senha}, vendedor: {self.__vendedor}"


class Usuarios(CRUD):
    @classmethod
    def salvar(cls):
        with open("usuarios_data.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, indent=4, default=lambda obj: {"id": obj.id, "nome": obj.nome, "email": obj.email, "senha": obj.senha, "vendedor": obj.vendedor})

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("usuarios_data.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Usuario(obj["id"], obj["nome"], obj["email"], obj["senha"], obj["vendedor"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
