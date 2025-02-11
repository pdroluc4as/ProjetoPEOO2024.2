import json
from models.CRUD import CRUD

class Item:
    def __init__(self, id, id_pedido, id_produto, unidade, presente):
        self.id = id
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.unidade = unidade
        self.presente = presente

    def __str__(self):
        return f"id: {self.id}, id_pedido: {self.id_pedido}, id_produto: {self.id_produto}, unidades: {self.unidade}, presente: {self.presente}"
    


class Itens(CRUD):
  @classmethod
  def salvar(cls):
    with open("itens.json", mode="w") as arquivo:   
      json.dump(cls.objetos, arquivo, indent = 4, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("itens.json", mode="r") as arquivo:   
        texto = json.load(arquivo)
        for obj in texto:   
          c = Item(obj["id"], obj["id_pedido"], obj["id_produto"], obj["unidade"], obj["presente"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass