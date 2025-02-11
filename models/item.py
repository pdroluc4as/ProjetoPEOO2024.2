import json
from CRUD import CRUD

class Item:
    def __init__(self, id, id_pedido, id_produto, unidade, presente):
        self.__id = id
        self.__id_pedido = id_pedido
        self.__id_produto = id_produto
        self.__unidade = unidade
        self.__presente = presente
    
    # Getters
    @property
    def id(self):
        return self.__id

    @property
    def id_pedido(self):
        return self.__id_pedido

    @property
    def id_produto(self):
        return self.__id_produto

    @property
    def unidade(self):
        return self.__unidade

    @property
    def presente(self):
        return self.__presente

    # Setters
    @id.setter
    def id(self, novo_id):
        self.__id = novo_id

    @id_pedido.setter
    def id_pedido(self, novo_id_pedido):
        self.__id_pedido = novo_id_pedido

    @id_produto.setter
    def id_produto(self, novo_id_produto):
        self.__id_produto = novo_id_produto

    @unidade.setter
    def unidade(self, nova_unidade):
        self.__unidade = nova_unidade

    @presente.setter
    def presente(self, novo_presente):
        self.__presente = novo_presente

    def __str__(self):
        return f"id: {self.__id}, id_pedido: {self.__id_pedido}, id_produto: {self.__id_produto}, unidades: {self.__unidade}, presente: {self.__presente}"


class Itens(CRUD):
  @classmethod
  def salvar(cls):
    with open("itens.json", mode="w") as arquivo:   
      json.dump(cls.objetos, arquivo, indent = 4, default=lambda obj: {"id": obj.id, "id_pedido": obj.id_pedido, "id_produto": obj.id_produto, "unidade": obj.unidade, "presente": obj.presente})

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