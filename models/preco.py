import json
from models.CRUD import CRUD

class Preco:
    def __init__(self, id, data):
        self.__id = id
        self.__id_produto = 0
        self.__data = data

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_produto(self):
        return self.__id_produto
        
    @property
    def data(self):
        return self.__data

    # Setters
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @id_produto.setter
    def id_produto(self, novo_id_produto):
        self.__id_produto = novo_id_produto
        
    @id_produto.setter
    def data(self, novo_data):
        self.__data = novo_data

    def __str__(self):
        return f"id: {self.__id}, id_produto: {self.__id_produto}, data: {self.__data}"
    


class Precos(CRUD):
  @classmethod
  def salvar(cls):
    with open("precos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent = 4 , default=lambda obj: {"id": obj.id, "id_produto": obj.id_produto, "data": obj.data})

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("precos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Preco(obj["id"], obj["id_produto"], obj["data"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass