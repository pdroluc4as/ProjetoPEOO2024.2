import json
from CRUD import CRUD

class Categoria:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def __str__(self):
        return f"id: {self.__id}, nome: {self.__nome}"
    
    
    def get_id(self):
        return self.__id

    
    def get_nome(self):
        return self.__nome

    
    def set_id(self, novo_id):
        self.__id = novo_id

    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome



class Categorias(CRUD):
  @classmethod
  def salvar(cls):
    with open("categorias.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent = 4, default=lambda obj: {"id": obj.get_id(), "nome": obj.get_nome()})

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("categorias.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Categoria(obj["id"], obj["nome"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass



c = Categoria(1, "Eletronicos")

Categorias.inserir(c)
