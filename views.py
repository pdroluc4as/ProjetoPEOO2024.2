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
        View.usuario_inserir("admin", "admin", "1234", False)
    # Criar Admin

    # usuario
    @staticmethod
    def usuario_inserir(nome, email, senha, vendedor):
        c = Usuario(0, nome, email, senha, vendedor)
        Usuarios.inserir(c)

    @staticmethod
    def usuario_listar():
        return Usuarios.listar()    

    @staticmethod
    def usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    @staticmethod
    def usuario_atualizar(id, nome, email, senha, vendedor):
        c = Usuario(id, nome, email, senha, vendedor)
        Usuarios.atualizar(c)

    @staticmethod
    def usuario_excluir(usuario):
        Usuarios.excluir(usuario)    

    @staticmethod
    def usuario_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.email == email and c.senha == senha and c.vendedor == False:
                return {"id": c.id, "nome": c.nome}
        return None

    @staticmethod
    def vendedor_autenticar(email, senha):
        for c in View.usuario_listar():
            if c.email == email and c.senha == senha and c.vendedor == True:
                return {"id": c.id, "nome": c.nome}
        return None
    # Cliente

    # Produto
    @staticmethod
    def produto_inserir(id_categoria, estado_de_uso, nome, preco, estoque):
        p = Produto(0, id_categoria, estado_de_uso, nome, preco, estoque)
        Produtos.inserir(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()

    @staticmethod
    def produto_listar_id(id):
        return Produtos.listar_id(id)

    @staticmethod
    def produto_atualizar(id, id_categoria, estado_de_uso, nome, preco, estoque):
        produtos = Produtos.listar()
        for produto in produtos:
            if produto.id == id:
                produto.id_categoria = id_categoria
                produto.estado_de_uso = estado_de_uso
                produto.nome = nome
                produto.preco = preco
                produto.estoque = estoque
                Produtos.salvar() # Salvar as alterações
                return

    @staticmethod
    def produto_excluir(produto):
        Produtos.excluir(produto)

    def produto_listar_disponiveis():
        produtos = View.produto_listar()
        disponiveis = []
        for h in produtos:
            disponiveis.append(h)
        return disponiveis
    # Produto

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
    # Preços

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
    def pedido_excluir(pedido):
        Pedidos.excluir(pedido)
    # Pedido

    # Item
    @staticmethod
    def item_inserir(id_pedido, id_produto, unidade, presente):
        i = Item(0, id_pedido, id_produto, unidade, presente)
        Itens.inserir(i)

    @staticmethod
    def item_listar():
        return Itens.listar()

    @staticmethod
    def item_listar_id(id):
        return Itens.listar_id(id)

    @staticmethod
    def item_atualizar(id, id_pedido, id_produto, unidade, presente):
        i = Item(id, id_pedido, id_produto, unidade, presente)
        Itens.atualizar(i)

    @staticmethod
    def item_excluir(id):
        Itens.excluir(id)
    # Item

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
    def categoria_excluir(categoria):
        Categorias.excluir(categoria)
    # Categoria