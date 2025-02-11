import json
from models.CRUD import CRUD

class Preco:
    def __init__(self, id, id_produto):
        self.id = id
        self.id_produto = id_produto


    def __str__(self):
        return f"id: {self.id}, id_produto: {self.id_produto}"
    


class Precos(CRUD):
  @classmethod
  def salvar(cls):
    with open("precos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent = 4 ,default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("precos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Preco(obj["id"], obj["id_produto"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass