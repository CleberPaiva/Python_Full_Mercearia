from datetime import datetime

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendido: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now()):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida   
        self.data = data     

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, endereco, categoria)
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.categoria = categoria    

class Pessoa:
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    def __init__(self, ctps, nome, telefone, cpf, email, endereco):
            self.ctps = ctps
            super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)

          
