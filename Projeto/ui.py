from services import Service

class UI:
    @staticmethod
    def main():
        op = 0 
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    @staticmethod
    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Sair")
        return int(input("Digite a opção: "))

    @staticmethod
    def inserir():
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        Service.inserir_cliente(nome, email, fone)
    @staticmethod
    def listar():
        for c in Service.listar_clientes():
            print(c)
    @staticmethod
    def atualizar():
        UI.listar()
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        Service.atualizar_cliente(id, nome, email, fone)
    @staticmethod
    def excluir():
        UI.listar()
        id = int(input("informe o id: "))
        Service.excluir_cliente(id)

UI.main()