import json
import datetime
from models.CRUD import CRUD

class Pedido:
    def __init__(self, id, id_cliente, previsao, entrega, nota_fiscal, status):
        self.__id = id
        self.__id_cliente = id_cliente
        self.__previsao = previsao
        self.__entrega = entrega
        self.__nota_fiscal = nota_fiscal
        self.__status = status
        

    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_cliente(self):
        return self.__id_cliente
    
    @property
    def previsao(self):
        return self.__previsao

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

    @id_cliente.setter
    def id_cliente(self, novo_id_cliente):
        self.__id_cliente = novo_id_cliente

    @previsao.setter
    def previsao(self, novo_previsao):
        self.__previsao = novo_previsao

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
        return f"id: {self.__id}, id_usuario: {self.__id_cliente}, previsao: {self.__previsao}, entrega: {self.__entrega}, nota_fiscal: {self.__nota_fiscal}, status: {self.__status}"
    


class Pedidos(CRUD):
  @classmethod
  def salvar(cls):
    with open("pedidos_data.json", mode="w") as arquivo:   
      json.dump(cls.objetos, arquivo, indent = 4, default=lambda obj: {"id": obj.id, "id_cliente": obj.id_cliente, "previsao": obj.previsao, "entrega": obj.entrega, "nota_fiscal": obj.nota_fiscal, "status": obj.status})

  @classmethod
  def abrir(cls):
        cls.objetos = []
        try:
            with open("pedidos_data.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    # Converter strings para objetos datetime
                    previsao = datetime.datetime.strptime(obj["previsao"], "%d/%m/%Y %H:%M")
                    entrega = datetime.datetime.strptime(obj["entrega"], "%d/%m/%Y %H:%M")
                    c = Pedido(obj["id"], obj["id_cliente"], previsao, entrega, obj["nota_fiscal"], obj["status"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass