import json
from models.CRUD import CRUD

class Pedido:
    def __init__(self, id, id_usuario, data, entrega, nota_fiscal, status):
        self.__id = id
        self.__id_usuario = id_usuario
        self.__data = data
        self.__entrega = entrega
        self.__nota_fiscal = nota_fiscal
        self.__status = status

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_usuario(self):
        return self.__id_usuario
    
    @property
    def data(self):
        return self.__data

    @property
    def entrega(self):
        return self.__entrega

    @property
    def nota_fiscal(self):
        return self.__nota_fiscal

    @property
    def status(self):
        return self.__status

    # Setters
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @id_usuario.setter
    def id_usuario(self, novo_id_usuario):
        self.__id_usuario = novo_id_usuario

    @data.setter
    def data(self, novo_data):
        self.__data = novo_data

    @entrega.setter
    def entrega(self, nova_entrega):
        self.__entrega = nova_entrega

    @nota_fiscal.setter
    def nota_fiscal(self, nova_nota_fiscal):
        self.__nota_fiscal = nova_nota_fiscal

    @status.setter
    def status(self, novo_status):
        self.__status = novo_status

    def __str__(self):
        return f"id: {self.__id}, id_usuario: {self.__id_usuario}, data: {self.__data}, entrega: {self.__entrega}, nota_fiscal: {self.__nota_fiscal}, status: {self.__status}"
    


class Pedidos(CRUD):
  @classmethod
  def salvar(cls):
    with open("pedidos.json", mode="w") as arquivo:   
      json.dump(cls.objetos, arquivo, indent = 4, default=lambda obj: {"id": obj.id, "id_usuario": obj.id_usuario, "data": obj.data, "entrega": obj.entrega, "nota_fiscal": obj.nota_fiscal, "status": obj.status})

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("pedidos.json", mode="r") as arquivo:   
        texto = json.load(arquivo)
        for obj in texto:   
          c = Pedido(obj["id"], obj["id_usuario"], obj["data"], obj["entrega"], obj["nota_fiscal"], obj["status"])
          cls.objetos.append(c)
    except FileNotFoundError:
      pass