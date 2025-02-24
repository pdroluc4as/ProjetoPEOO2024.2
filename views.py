from models.categoria import Categoria, Categorias
from models.item import Item, Itens
from models.pedido import Pedido, Pedidos
from models.preco import Preco, Precos
from models.produtos import Produto, Produtos
from models.cliente import Cliente, Clientes
from models.vendedor import Vendedor, Vendedores

class View:
    # Criar Admin
    @staticmethod
    def usuario_admin():
        for c in View.cliente_listar():
            if c.email == "admin":
                return
        View.cliente_inserir("admin", "admin", "1234")
    # Criar Admin

    # Cliente
    @staticmethod
    def cliente_inserir(nome, email, senha):
        c = Cliente(0, nome, email, senha)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar()    

    @staticmethod
    def cliente_listar_id(id):
        return Clientes.listar_id(id)    

    @staticmethod
    def cliente_atualizar(id, nome, email, senha):
        c = Cliente(id, nome, email, senha)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(cliente):
        Clientes.excluir(cliente)    

    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id": c.id, "nome": c.nome}
        return None
    # Cliente

    # Vendedor
    @staticmethod
    def vendedor_inserir(nome, email, senha):
        c = Vendedor(0, nome, email, senha)
        Vendedores.inserir(c)

    @staticmethod
    def vendedor_listar():
        return Vendedores.listar()    

    @staticmethod
    def vendedor_listar_id(id):
        return Vendedores.listar_id(id)    

    @staticmethod
    def vendedor_atualizar(id, nome, email, senha):
        c = Vendedor(id, nome, email, senha)
        Vendedores.atualizar(c)

    @staticmethod
    def vendedor_excluir(vendedor):
        Vendedores.excluir(vendedor)    

    @staticmethod
    def vendedor_autenticar(email, senha):
        for c in View.vendedor_listar():
            if c.email == email and c.senha == senha:
                return {"id": c.id, "nome": c.nome}
        return None
    # Vendedor

    # Produto
    @staticmethod
    def produto_inserir(id_categoria, vendedor, estado_de_uso, nome, preco, estoque):
        p = Produto(0, id_categoria, vendedor.id, estado_de_uso, nome, preco, estoque)
        Produtos.inserir(p)

    @staticmethod
    def produto_listar():
        return Produtos.listar()

    @staticmethod
    def produto_listar_id(id):
        return Produtos.listar_id(id)

    @staticmethod
    def produto_atualizar(id, id_categoria, vendedor, estado_de_uso, nome, preco, estoque):
        produtos = Produtos.listar()
        for produto in produtos:
            if produto.id == id:
                produto.id_categoria = id_categoria
                produto.id_vendedor = vendedor.id
                produto.estado_de_uso = estado_de_uso
                produto.nome = nome
                produto.preco = preco
                produto.estoque = estoque
                Produtos.salvar() # Salvar as alterações
                return

    @staticmethod
    def produto_excluir(produto):
        Produtos.excluir(produto)
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