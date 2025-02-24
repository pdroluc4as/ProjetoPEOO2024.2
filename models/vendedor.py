import json
from models.CRUD import CRUD
from models.usuario import Usuario

class Vendedor(Usuario):
    def __init__(self, id, nome, email, senha):
        super().__init__(id, nome, email, senha)

class Vendedores(CRUD):
    @classmethod
    def salvar(cls):
        with open("vendedores_data.json", mode="w") as arquivo:   
            json.dump(cls.objetos, arquivo, indent=4, default=lambda obj: {"id": obj.id, "nome": obj.nome, "email": obj.email, "senha": obj.senha})

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("vendedores_data.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Vendedor(obj["id"], obj["nome"], obj["email"], obj["senha"])
                    cls.objetos.append(c)  # Corrigida a indentação
        except FileNotFoundError:
            pass