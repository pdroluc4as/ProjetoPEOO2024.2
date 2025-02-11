import json
from models.CRUD import CRUD

class Pedido:
    def __init__(self, id, id_usuario, entrega, nota_fiscal, status):
        self.id = id
        self.id_usuario = id_usuario
        self.entrega = entrega
        self.nota_fiscal = nota_fiscal
        self.status - status

    def __str__(self):
        return f"id: {self.id}, id_usuario: {self.id_usuario}, entrega: {self.entrega}, nota_fiscal: {self.nota_fiscal}, status: {self.status}"
    


class Pedidos(CRUD):
  @classmethod
  def salvar(cls):
    with open("pedidos.json", mode="w") as arquivo:   
      json.dump(cls.objetos, arquivo, indent = 4, default = vars)

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("pedidos.json", mode="r") as arquivo:   
        texto = json.load(arquivo)
        for obj in texto:   
          c = Pedido(obj["id"], obj["entrega"], obj["nota_fiscal"], obj["status"], obj["id_usuario"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass