class Cliente: 
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | E-mail: {self.__email} | Fone: {self.__fone}"
    
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def to_json(self):
        clientes = {}
        clientes["id"] = self.__id
        clientes["nome"] = self.__nome
        clientes["email"] = self.__email
        clientes["fone"] = self.__fone
        return clientes

    @staticmethod
    def from_json(clientes):
        return Cliente(clientes["id"], clientes["nome"], clientes["email"], clientes["fone"])

    