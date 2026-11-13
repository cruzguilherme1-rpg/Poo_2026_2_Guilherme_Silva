from Cliente import Cliente
from ClienteDAO import ClienteDAO

class UI:
    def main():
        op = 0 
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()

    def menu():
        print("1 - Inserir, 2 - Listar, 3 - Atualizar, 4 - Excluir, 9 - Sair")
        return int(input("Digite a opção: "))

    def inserir():
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        c = Cliente(0, nome, email, fone)
        ClienteDAO().inserir(c)
    def listar():
        for c in ClienteDAO().listar():
            print(c)
    def atualizar():
        id = int(input("informe o id: "))
        nome = input("informe o nome: ")
        email = input("informe o e-mail: ")
        fone = input("informe o fone: ")
        c = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(c)
    def excluir():
        id = int(input("informe o id: "))
        ClienteDAO().excluir(id)

UI.main()