from models.categoria import Categoria, Categorias
from models.item import Item, Itens
from models.pedido import Pedido, Pedidos
from models.preco import Preco, Precos
from models.produtos import Produto, Produtos
from models.usuario import Usuario, Usuarios

class View:
    # Criar Admin
    @staticmethod
    def usuario_admin():
        for c in View.usuario_listar():
            if c.email == "admin":
                return
        View.usuario_inserir("admin", "admin", "1234")

    # Usuário
    @staticmethod
    def usuario_inserir(nome, email, senha):
        c = Usuario(0, nome, email, senha)
        Usuarios.inserir(c)

    @staticmethod
    def usuario_listar():
        return Usuarios.listar()    

    @staticmethod
    def usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    @staticmethod
    def usuario_atualizar(id, nome, email, senha):
        c = Usuario(id, nome, email, senha)
        Usuarios.atualizar(c)

    @staticmethod
    def usuario_excluir(id):
        Usuarios.excluir(id)    

    @staticmethod
    def usuario_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.email == email and c.senha == senha:
                return {"id": c.id, "nome": c.nome}
        return None

    # Produto
    @staticmethod
    def produto_inserir(estado_de_uso, id_categoria, nome, preco, estoque):
        p = Produto(0, estado_de_uso, id_categoria, nome, preco, estoque)
        Produtos.inserir(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()

    @staticmethod
    def produto_listar_id(id):
        return Produtos.listar_id(id)

    @staticmethod
    def produto_atualizar(id, estado_de_uso, id_categoria, nome, preco, estoque):
        p = Produto(id, estado_de_uso, id_categoria, nome, preco, estoque)
        Produtos.atualizar(p)

    @staticmethod
    def produto_excluir(id):
        Produtos.excluir(id)

    # Preços
    @staticmethod
    def preco_inserir(id_produto, data):
        p = Preco(0, id_produto, data)
        Precos.inserir(p)

    @staticmethod
    def preco_listar():
        return Precos.listar()

    @staticmethod
    def preco_listar_id(id):
        return Precos.listar_id(id)

    @staticmethod
    def preco_atualizar(id, id_produto, data):
        p = Preco(id, id_produto, data)
        Precos.atualizar(p)

    @staticmethod
    def preco_excluir(id):
        Precos.excluir(id)

    # Pedido
    @staticmethod
    def pedido_inserir(id_usuario, data, entrega, nota_fiscal, status):
        p = Pedido(0, id_usuario, data, entrega, nota_fiscal, status)
        Pedidos.inserir(p)

    @staticmethod
    def pedido_listar():
        return Pedidos.listar()

    @staticmethod
    def pedido_listar_id(id):
        return Pedidos.listar_id(id)

    @staticmethod
    def pedido_atualizar(id, id_usuario, data, entrega, nota_fiscal, status):
        p = Pedido(id, id_usuario, data, entrega, nota_fiscal, status)
        Pedidos.atualizar(p)

    @staticmethod
    def pedido_excluir(id):
        Pedidos.excluir(id)

    # Item
    @staticmethod
    def item_inserir(id_pedido, id_produto, preco, unidade, presente):
        i = Item(0, id_pedido, id_produto, preco, unidade, presente)
        Itens.inserir(i)

    @staticmethod
    def item_listar():
        return Itens.listar()

    @staticmethod
    def item_listar_id(id):
        return Itens.listar_id(id)

    @staticmethod
    def item_atualizar(id, id_pedido, id_produto, preco, unidade, presente):
        i = Item(id, id_pedido, id_produto, preco, unidade, presente)
        Itens.atualizar(i)

    @staticmethod
    def item_excluir(id):
        Itens.excluir(id)

    # Categoria
    @staticmethod
    def categoria_inserir(nome):
        c = Categoria(0, nome)
        Categorias.inserir(c)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()

    @staticmethod
    def categoria_listar_id(id):
        return Categorias.listar_id(id)

    @staticmethod
    def categoria_atualizar(id, nome):
        c = Categoria(id, nome)
        Categorias.atualizar(c)

    @staticmethod
    def categoria_excluir(id):
        Categorias.excluir(id)
