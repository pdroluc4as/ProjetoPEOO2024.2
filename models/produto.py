import json
from models.CRUD import CRUD

class Produto:
    def __init__(self, id, id_categoria, estado_de_uso, nome, preco, estoque, data):
        self.__id = id
        self.__id_categoria = id_categoria
        self.__estado_de_uso = estado_de_uso
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
        self.__data = data

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_categoria(self):
        return self.__id_categoria
    
    @property
    def estado_de_uso(self):
        return self.__estado_de_uso

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def estoque(self):
        return self.__estoque
    
    @property
    def data(self):
        return self.__data

    # Setters
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @id_categoria.setter
    def id_categoria(self, novo_id_categoria):
        self.__id_categoria = novo_id_categoria

    @estado_de_uso.setter
    def estado_de_uso(self, novo_estado):
        self.__estado_de_uso = novo_estado
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @estoque.setter
    def estoque(self, novo_estoque):
        self.__estoque = novo_estoque
    
    @data.setter
    def data(self, novo_data):
        self.__data = novo_data

    def __str__(self):
        return f"id: {self.__id}, id_categoria: {self.__id_categoria}, estado_de_uso: {self.__estado_de_uso}, nome: {self.__nome}, preco: {self.__preco:.2f}, estoque: {self.__estoque}, data: {self.__data}"


class Produtos(CRUD):
    @classmethod
    def salvar(cls):
        with open("produtos_data.json", mode="w") as arquivo:   # w - write
            json.dump(cls.objetos, arquivo, indent=4, default=lambda obj: {"id": obj.id, "id_categoria": obj.id_categoria, "estado_de_uso": obj.estado_de_uso, "nome": obj.nome, "preco": obj.preco, "estoque": obj.estoque, "data": obj.data})

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos_data.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Produto(obj["id"], obj["id_categoria"], obj["estado_de_uso"], obj["nome"], obj["preco"], obj["estoque"], obj["data"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass
