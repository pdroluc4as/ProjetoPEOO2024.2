import json
from models.CRUD import CRUD

class Item:
    def __init__(self, id, id_categoria, estado_de_uso, preco, estoque):
        self.id = id
        self.id_categoria = id_categoria
        self.estado_de_uso = estado_de_uso
        self.preco = preco
        self.estoque = estoque

    def __str__(self):
        return f"id: {self.id}, id_categoria: {self.id_categoria}, estado_de_uso: {self.estado_de_uso}, preco: {self.preco}, estoque: {self.estoque}"
    


class Produtos(CRUD):
  @classmethod
  def salvar(cls):
    with open("produtos.json", mode="w") as arquivo:   # w - write
      json.dump(cls.objetos, arquivo, indent = 4, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("produtos.json", mode="r") as arquivo:   # r - read
        texto = json.load(arquivo)
        for obj in texto:   
          c = Produtos(obj["id"], obj["id_categoria"], obj["estado_de_uso"], obj["preco"], obj["estoque"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass