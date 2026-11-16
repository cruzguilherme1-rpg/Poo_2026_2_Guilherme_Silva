class Cliente: 
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | E-mail: {self.email} | Fone: {self.fone}"
    
    def set_id(self, id): self.id = id
    def set_nome(self, nome): self.nome = nome
    def set_email(self, email): self.email = email
    def set_fone(self, fone): self.fone = fone

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["email"] = self.email
        dic["fone"] = self.fone
        return dic

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])

    