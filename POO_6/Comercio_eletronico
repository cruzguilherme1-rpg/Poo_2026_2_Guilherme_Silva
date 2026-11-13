import json
import os

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    # Getters e Setters
    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_nome(self) -> str:
        return self.__nome

    def set_nome(self, nome: str):
        self.__nome = nome

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_fone(self) -> str:
        return self.__fone

    def set_fone(self, fone: str):
        self.__fone = fone


    def __str__(self) -> str:
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Fone: {self.__fone}"


    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }
    
    @staticmethod
    def from_dict(d: dict):
        return Cliente(d["id"], d["nome"], d["email"], d["fone"])



class ClienteDAO:
    objetos = []
    __arquivo = "clientes.json"

    @classmethod
    def Inserir(cls, obj: Cliente) -> None:
        cls.Abrir()
        cls.objetos.append(obj)
        cls.Salvar()

    @classmethod
    def Listar(cls) -> list:
        cls.Abrir()
        return cls.objetos

    @classmethod
    def Listar_Id(cls, id: int) -> Cliente:
        cls.Abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def Atualizar(cls, obj: Cliente) -> None:
        cls.Abrir()
        existente = cls.Listar_Id(obj.get_id())
        if existente:
            existente.set_nome(obj.get_nome())
            existente.set_email(obj.get_email())
            existente.set_fone(obj.get_fone())
            cls.Salvar()

    @classmethod
    def Excluir(cls, obj: Cliente) -> None:
        cls.Abrir()
        existente = cls.Listar_Id(obj.get_id())
        if existente:
            cls.objetos.remove(existente)
            cls.Salvar()

    @classmethod
    def Abrir(cls) -> None:
        cls.objetos = []
        if os.path.exists(cls.__arquivo):
            with open(cls.__arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                for item in dados:
                    cls.objetos.append(Cliente.from_dict(item))

    @classmethod
    def Salvar(cls) -> None:
        dados = [obj.to_dict() for obj in cls.objetos]
        with open(cls.__arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

class UI:
    @staticmethod
    def Main():
        op = -1
        while op != 0:
            op = UI.Menu()
            if op == 1:
                UI.Cliente_Listar()
            elif op == 2:
                UI.Cliente_Inserir()
            elif op == 3:
                UI.Cliente_Atualizar()
            elif op == 4:
                UI.Cliente_Excluir()
            elif op == 0:
                print("\nPrograma finalizado com sucesso!")
            else:
                print("\nOpção inválida! Tente novamente.")

    @staticmethod
    def Menu() -> int:
        print("\n" + "=" * 30)
        print("    SISTEMA DE CLIENTES")
        print("=" * 30)
        print("1 - Listar Clientes")
        print("2 - Inserir Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("0 - Sair")
        print("=" * 30)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    @staticmethod
    def Cliente_Listar():
        print("\n--- Lista de Clientes ---")
        clientes = ClienteDAO.Listar()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for c in clientes:
                print(c)

    @staticmethod
    def Cliente_Inserir():
        print("\n--- Inserir Cliente ---")
        try:
            id = int(input("Informe o ID: "))
            if ClienteDAO.Listar_Id(id) is not None:
                print("Erro: Já existe um cliente cadastrado com esse ID.")
                return
            nome = input("Informe o Nome: ")
            email = input("Informe o E-mail: ")
            fone = input("Informe o Telefone: ")

            novo_cliente = Cliente(id, nome, email, fone)
            ClienteDAO.Inserir(novo_cliente)
            print("Cliente inserido com sucesso!")
        except ValueError:
            print("ID inválido. Operação cancelada.")

    @staticmethod
    def Cliente_Atualizar():
        print("\n--- Atualizar Cliente ---")
        try:
            id = int(input("Informe o ID do cliente que deseja atualizar: "))
            cliente = ClienteDAO.Listar_Id(id)
            if cliente is None:
                print("Cliente não encontrado.")
                return

            print(f"Dados atuais: {cliente}")
            nome = input("Informe o novo Nome: ")
            email = input("Informe o novo E-mail: ")
            fone = input("Informe o novo Telefone: ")

            cliente_atualizado = Cliente(id, nome, email, fone)
            ClienteDAO.Atualizar(cliente_atualizado)
            print("Cliente atualizado com sucesso!")
        except ValueError:
            print("ID inválido. Operação cancelada.")

    @staticmethod
    def Cliente_Excluir():
        print("\n--- Excluir Cliente ---")
        try:
            id = int(input("Informe o ID do cliente que deseja excluir: "))
            cliente = ClienteDAO.Listar_Id(id)
            if cliente is None:
                print("Cliente não encontrado.")
                return

            ClienteDAO.Excluir(cliente)
            print("Cliente excluído com sucesso!")
        except ValueError:
            print("ID inválido. Operação cancelada.")

UI.Main()