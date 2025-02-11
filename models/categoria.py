import json
from models.CRUD import CRUD

class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


    def __str__(self):
        return f"id: {self.id}, nome: {self.nome}"
    




class Categorias(CRUD):
  @classmethod
  def salvar(cls):
    with open("categorias.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent = 4, default = vars)

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