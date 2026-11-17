from datetime import datetime
from services import Service

def parse_data(data_str):
    formatos = ("%d/%m/%Y %H:%M:%S", "%d %m %Y %H %M %S")
    for formato in formatos:
        try:
            return datetime.strptime(data_str, formato)
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use dd/mm/aaaa hh:mm:ss ou dd mm aaaa hh mm ss.")

class UI:
    @staticmethod
    def main():
        op = 0 
        while op != 14:
            op = UI.menu()
            if op == 1: UI.inserir_cliente()
            if op == 2: UI.listar_clientes()
            if op == 3: UI.atualizar_cliente()
            if op == 4: UI.excluir_cliente()
            if op == 5: UI.inserir_venda()
            if op == 6: UI.listar_vendas()
            if op == 7: UI.listar_vendas_por_id()
            if op == 8: UI.atualizar_venda()
            if op == 9: UI.excluir_venda()
            if op == 10: UI.inserir_produto()
            if op == 11: UI.listar_produtos()
            if op == 12: UI.atualizar_produto()
            if op == 13: UI.excluir_produto()
    @staticmethod
    def menu():
        print("1 - Inserir Cliente, 2 - Listar Clientes, 3 - Atualizar Cliente, 4 - Excluir Cliente, 5 - Inserir Venda, 6 - Listar Vendas, 7 - Listar Vendas por ID, 8 - Atualizar Venda, 9 - Excluir Venda, 10 - Inserir Produto, 11 - Listar Produtos, 12 - Atualizar Produto, 13 - Excluir Produto, 14 - Sair")
        return int(input("Digite a opção: "))

    @staticmethod
    def inserir_cliente():
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        Service.inserir_cliente(nome, email, fone)
    @staticmethod
    def listar_clientes():
        for c in Service.listar_clientes():
            print(c)
    @staticmethod
    def atualizar_cliente  ():
        UI.listar_clientes()
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        Service.atualizar_cliente(id, nome, email, fone)
    @staticmethod
    def excluir_cliente():
        UI.listar_clientes()
        id = int(input("informe o id: "))
        Service.excluir_cliente(id)

    @staticmethod
    def inserir_venda():
        id = int(input("informe o id da venda: "))
        data_str = input("informe a data (dd/mm/aaaa hh:mm:ss ou dd mm aaaa hh mm ss): ")
        data = parse_data(data_str)
        carrinho = input("informe o carrinho (digite Sim ou Não): ")
        if carrinho == "Sim": carrinho = True
        if carrinho == "Não": carrinho = False
        total = input("calcular o total (digite Sim ou Não): ")
        id_cliente = int(input("informe o id do cliente: "))
        Service.inserir_venda(id, data, carrinho, total, id_cliente)

    @staticmethod
    def listar_vendas():
        for v in Service.listar_vendas():
            print(v)
    
    @staticmethod
    def listar_vendas_por_id():
        id = int(input("informe o id da venda: "))
        v = Service.listar_vendas_por_id(id)
        if v != None:
            print(v)
        else:
            print("Venda não encontrada")

    @staticmethod
    def atualizar_venda():
        UI.listar_vendas()
        id = int(input("informe o id da venda: "))
        data_str = input("informe a data (dd/mm/aaaa hh:mm:ss ou dd mm aaaa hh mm ss): ")
        data = parse_data(data_str)
        carrinho = input("informe o carrinho (digite Sim ou Não): ")
        if carrinho == "Sim": carrinho = True
        if carrinho == "Não": carrinho = False
        total = input("calcular o total (digite Sim ou Não): ")
        id_cliente = int(input("informe o id do cliente: "))
        Service.atualizar_venda(id, data, carrinho, total, id_cliente)
    
    @staticmethod
    def excluir_venda():
        UI.listar_vendas()
        id = int(input("informe o id da venda: "))
        Service.excluir_venda(id)

    @staticmethod
    def inserir_produto():
        nome = input("informe o nome do produto: ")
        preco = float(input("informe o preço do produto: "))
        quantidade = int(input("informe a quantidade do produto: "))
        Service.inserir_produto(nome, preco, quantidade)

    @staticmethod
    def listar_produtos():
        for p in Service.listar_produtos():
            print(p)

    @staticmethod
    def atualizar_produto():
        UI.listar_produtos()
        id = int(input("informe o id do produto: "))
        nome = input("informe o nome do produto: ")
        preco = float(input("informe o preço do produto: "))
        quantidade = int(input("informe a quantidade do produto: "))
        Service.atualizar_produto(id, nome, preco, quantidade)

    @staticmethod
    def excluir_produto():
        UI.listar_produtos()
        id = int(input("informe o id do produto: "))
        Service.excluir_produto(id)

UI.main()