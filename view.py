from models.categoria import Categoria, Categorias
from models.item import Item, Itens
from models.pedido import Pedido, Pedidos
from models.preco import Preco, Precos
from models.produtos import Produto, Produtos
from models.usuario import Usuario, Usuarios

class View:
    #CRIAR ADMIN
    def usuario_admin():
        for c in View.cliente_listar():
            if c.email == "admin": return
        View.cliente_inserir("admin", "admin", "1234", "1234")

    #CLIENTE
    def usuario_inserir(nome, email, senha):
        c = Usuario(0, nome, email, senha)
        Usuarios.inserir(c)

    def usuario_listar():
        return Usuarios.listar()    

    def usuario_listar_id(id):
        return Usuarios.listar_id(id)    

    def usuario_atualizar(id, nome, email, senha):
        c = Usuario(id, nome, email, senha)
        Usuarios.atualizar(c)

    def usuario_excluir(id):
        c = Usuario(id, "", "", "",)
        Usuarios.excluir(c)    

    def usuario_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.email == email and c.senha == senha:
                return {"id" : c.id, "nome" : c.nome }
        return None
    #CLIENTE

    #Produtos
    def produto_inserir(estado_de_uso, id_categoria, nome, preco, estoque):
        p = Produto(0)
        p.estado_de_uso = estado_de_uso
        p.nome = nome
        p.preco = preco
        p.estoque = estoque
        p.id_categoria = id_categoria
        Produtos.inserir(p)

    def produto_listar():
        return Produtos.listar()
    
    def produto_listar_id(id):
        return Produtos.listar_id(id)
    
    def produto_atualiazar(id, estado_de_uso, id_categoria, nome, preco, estoque):
        p = Produto(id, estado_de_uso, id_categoria, nome, preco, estoque)
        Produtos.atualizar(p)

    def produto_excluir(id):
        p = Produto(id, "", "", "", "")
        Produtos.excluir(p)
    #produtos

    #Precos
    def preco_inserir(id_produto, data):
        p = Preco(0, data)
        p.id_produto = id_produto
        Precos.inserir(p)

    def preco_listar():
        return Precos.listar()
    
    def preco_listar_id(id):
        return Precos.listar_id(id)
    
    def preco_atualiazar(id, id_produto, data):
        p = Preco(id, id_produto, data)
        Precos.atualizar(p)

    def preco_excluir(id):
        p = Preco(id, None)
        Precos.excluir(p)
    #Precos

    #Pedidos
    def pedido_inserir(id_usuario, data, entrega, nota_fiscal, status):
        p = Pedido(0, data)
        p.entrega = entrega
        p.id_usuario = id_usuario
        p.nota_fiscal = nota_fiscal
        p.status = status
        Pedidos.inserir(p)

    def pedido_listar():
        return Pedidos.listar()
    
    def pedido_listar_id(id):
        return Pedidos.listar_id(id)
    
    def pedido_atualiazar(id, id_usuario, data, entrega, nota_fiscal, status):
        p = Pedido(id, id_usuario, data, entrega, nota_fiscal, status)
        Pedidos.atualizar(p)

    def pedido_excluir(id):
        p = Pedidos(id, None)
        Pedidos.excluir(p)
    #Pedidos

    #Item
    def item_inserir(id_pedido, id_produto, preco, unidade, presente):
        i = Item(0, id_pedido, id_produto, preco, unidade, presente)
        Itens.inserir(i)

    def item_listar():
        return Itens.listar()
    
    def item_listar_id(id):
        return Itens.listar_id(id)
    
    def item_atualiazar(id, id_pedido, id_produto, preco, unidade, presente):
        i = Pedido(id, id_pedido, id_produto, preco, unidade, presente)
        Itens.atualizar(i)

    def item_excluir(id):
        i = Itens(id, None)
        Itens.excluir(i)
    #Item

    #Categoria
    def categoria_inserir(nome):
        c = Categoria(0, nome)
        Categorias.inserir(c)

    def categoria_listar():
        return Categorias.listar()
    
    def categoria_listar_id(id):
        return Categorias.listar_id(id)
    
    def categoria_atualiazar(id, nome):
        c = Categorias(id, nome)
        Categorias.atualizar(c)

    def categoria_excluir(id):
        c = Categorias(id, "")
        Categorias.excluir(c)
    #Categoria