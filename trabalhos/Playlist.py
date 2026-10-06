import datetime

class Musica: 
    def __init__(self, id, titulo, artista, album, temp_total):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_artista(artista)
        self.set_album(album)
        self.set_temp_total(temp_total)

    def set_id(self, id):
        if id < 0: raise ValueError("ID da música deve ser positivo")
        self.__id = id

    def set_titulo(self, titulo):
        if titulo == "": raise ValueError("Título deve ser informado")
        self.__titulo = titulo

    def set_artista(self, artista):
        if artista == "": raise ValueError("Artista deve ser informado")
        self.__artista = artista

    def set_album(self, album):
        if album == "": raise ValueError("Álbum deve ser informado")
        self.__album = album

    def set_temp_total(self, temp_total):
        self.__temp_total = temp_total

    def get_id(self): return self.__id
    def get_titulo(self): return self.__titulo
    def get_artista(self): return self.__artista
    def get_album(self): return self.__album
    def get_temp_total(self): return self.__temp_total

    def __str__(self):
        return f"{self.__titulo} - {self.__artista} ({self.__album})"

class PlayListItem:
    def __init__(self, id_identificador, playlist, musica, data_inclusao, seq_musica):
        self.set_id_identificador(id_identificador)
        self.set_id_playlist(playlist)
        self.set_id_musica(musica)
        self.set_data_inclusao(data_inclusao)
        self.set_seq_musica(seq_musica)

    def set_id_identificador(self, id_identificador):
        if id_identificador <= 0: raise ValueError("ID do item da playlist deve ser positivo")
        self.__id_identificador = id_identificador

    def set_id_playlist(self, playlist):
        if not isinstance(playlist, Playlist):
            raise ValueError("Playlist deve ser uma instância da classe Playlist")
        self.__id_playlist = playlist

    def set_id_musica(self, musica):
        if not isinstance(musica, Musica):
            raise ValueError("Música deve ser uma instância da classe Musica")
        self.__id_musica = musica

    def set_data_inclusao(self, data_inclusao):
        if not isinstance(data_inclusao, datetime.date):
            raise ValueError("Data de inclusão deve ser uma instância da classe datetime.date")
        self.__data_inclusao = data_inclusao

    def set_seq_musica(self, seq_musica):
        if seq_musica <= 0: raise ValueError("Sequência da música deve ser positiva")
        self.__seq_musica = seq_musica
        
    def get_id_identificador(self): return self.__id_identificador
    def get_id_playlist(self): return self.__id_playlist
    def get_id_musica(self): return self.__id_musica
    def get_data_inclusao(self): return self.__data_inclusao
    def get_seq_musica(self): return self.__seq_musica

    def __str__(self):
        data_fmt = self.__data_inclusao.strftime("%d/%m/%Y")
        return f"Posição {self.__seq_musica}: '{self.__id_musica.get_titulo()}' (Adicionada em: {data_fmt})"

class Playlist:
    def __init__(self, id, nome, descricao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.__itens = []

    def set_id(self, id):
        if id < 0: raise ValueError("ID deve ser positivo")
        self.__id = id

    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_descricao(self): return self.__descricao
    def get_itens(self): return self.__itens

    def inserir_item(self, item):
        self.__itens.append(item)
        # Mantém os itens ordenados pela sequência
        self.__itens.sort(key=lambda x: x.get_seq_musica())

    def obter_proxima_musica(self, seq_atual):
        for item in self.__itens:
            if item.get_seq_musica() == seq_atual + 1:
                return item.get_id_musica()
        return None

    def calcular_tempo_total(self):
        total = datetime.timedelta(0)
        for item in self.__itens:
            total += item.get_id_musica().get_temp_total()
        
        total_segundos = int(total.total_seconds())
        minutos = total_segundos // 60
        segundos = total_segundos % 60
        return f"{minutos}m {segundos}s"

    def __str__(self):
        return f"A playlist '{self.__nome}' (ID: {self.__id}) tem {len(self.__itens)} música(s) com tempo total de {self.calcular_tempo_total()}."

class UI:
    playlists = []
    musicas = []
    proximo_id_item = 1

    @staticmethod  
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1: UI.inserir_playlist()
            if op == 2: UI.listar_playlist()
            if op == 3: UI.inserir_musica()
            if op == 4: UI.listar_musica()
            if op == 5: UI.playlistem()

    @staticmethod
    def menu():
        print("\n1 - Inserir playlist | 2 - Listar playlists | 3 - Cadastrar música | 4 - Listar músicas | 5 - Vincular música à playlist (PlayListItem) | 10 - Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir_playlist(cls):
        id = int(input("Informe o ID da playlist: "))
        nome = input("Informe o nome da playlist: ")
        desc = input("Informe a descrição: ")
        x = Playlist(id, nome, desc)
        cls.playlists.append(x)
        print("Playlist criada com sucesso!")

    @classmethod
    def listar_playlist(cls):
        if not cls.playlists:
            print("Nenhuma playlist cadastrada.")
            return
        for x in cls.playlists: 
            print(x)

    @classmethod
    def inserir_musica(cls):
        id_m = int(input("Informe o ID da música: "))
        titulo = input("Informe o título da música: ")
        artista = input("Informe o artista: ")
        album = input("Informe o álbum: ")
        minutos = int(input("Informe a duração (minutos): "))
        segundos = int(input("Informe a duração (segundos): "))
        
        temp_total = datetime.timedelta(minutes=minutos, seconds=segundos)
        m = Musica(id_m, titulo, artista, album, temp_total)
        cls.musicas.append(m)
        print("Música cadastrada com sucesso!")

    @classmethod
    def listar_musica(cls):
        if not cls.musicas:
            print("Nenhuma música cadastrada.")
            return
        for m in cls.musicas: 
            print(f"ID {m.get_id()}: {m}")

    @classmethod
    def playlistem(cls):
        if not cls.playlists or not cls.musicas:
            print("Você precisa ter pelo menos uma playlist e uma música cadastrada antes!")
            return

        id_playlist = int(input("Informe o ID da playlist: "))
        playlist_obj = next((p for p in cls.playlists if p.get_id() == id_playlist), None)

        if not playlist_obj:
            print("Playlist não encontrada!")
            return

        id_musica = int(input("Informe o ID da música a ser vinculada: "))
        musica_obj = next((m for m in cls.musicas if m.get_id() == id_musica), None)

        if not musica_obj:
            print("Música não encontrada!")
            return

        seq_musica = int(input("Informe a sequência/posição dessa música na playlist: "))
        data_inclusao = datetime.date.today()

       
        item = PlayListItem(cls.proximo_id_item, playlist_obj, musica_obj, data_inclusao, seq_musica)
        cls.proximo_id_item += 1
        
        playlist_obj.inserir_item(item)

        
        print("\n--- DETALHES DO ITEM DA PLAYLIST ---")
        print(f"Música: {musica_obj.get_titulo()}")
        print(f"Playlist: {playlist_obj.get_nome()}")
        print(f"Data de Inclusão: {data_inclusao.strftime('%d/%m/%Y')}")
        
        proxima = playlist_obj.obter_proxima_musica(seq_musica)
        if proxima:
            print(f"Próxima música a ser tocada: {proxima.get_titulo()} - {proxima.get_artista()}")
        else:
            print("Próxima música a ser tocada: Nenhuma (é a última música da playlist até o momento)")

UI.main()