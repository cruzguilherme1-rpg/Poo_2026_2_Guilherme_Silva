class Musica: 
    def __init__(self, titulo, artista, album):
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)

    def set_titulo(self, titulo):
        if titulo == "": raise ValueError("titulo deve ser informado")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "": raise ValueError("artista deve ser informado")
        self.__artista = artista

    def set_album(self, album):
        if album == "": raise ValueError("album deve ser informado")
        self.__album = album

    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def __str__(self):
        return f"{self.__titulo} - `{self.__artista} - {self.__album}"

class Playlist:
    def __init__(self, nome, descricao):
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__musicas = []

    def set_nome(self, nome):
        if nome == "": raise ValueError("nome deve ser informado")
        self.__nome = nome
    def set_descricao(self, descricao):
        #if descricao == "": raise ValueError("descricao deve ser informado")
        self.__descricao = descricao

    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def inserir(self, m):
        self.__musicas.append(m)
    def listar(self):
        return self.__musicas
    def __str__(self):
        return f"A playlist {self.nome} tem {len(self.__musicas)} musica(s)"

class UI:
    playlist = []

    @staticmethod  
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlist()
            if op == 3: UI.inserir_musica()
            if op == 4: UI.listar_musica()

    @staticmethod
    def menu():
        print("1 - inserir playlist, 2 - listar playlist, 3 - inserir musica, 4 - listar musicas, 5 - fim")
        return int(input("escolha uma opção"))

    @classmethod
    def inserir_playlist(cls):
        nome = input("informe o nome da playlist: ")
        desc = input("informe a descrição: ")
        x = Playlist(nome, desc)
        cls.playlist.append(x)
        pass

    @classmethod
    def listar_playlist(cls):
        for x in cls.playlist: print(x)

    @classmethod
    def inserir_musica(cls):
        if len(cls.playlist) == 0:
            print("Insira uma playlist antes de inserir as músicas!")
            return
        for i,x in enumerate(cls.playlist):
            print (i, " - ",  x.get_nome())
        
        index = int(input("informe o numero da playlist: "))
        titulo = input("informe o titulo da musica: ")
        artista = input("informe o artista: ")
        album = input("informe o album: ")
        m = Musica(titulo, artista, album)
        cls.playlist[index].inserir(m)

    @classmethod
    def listar_musica():
        for x in cls.playlist:
            print("playlist", x.get_nome())
            for m in x.listar():
                print("   ", m)

UI.main()