from rich.panel import Panel
from rich import print


class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, game):
        self.favoritos.append(game)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue] {self.nome} [/]"
        conteudo += f'\nJogos favoritos:'
        for game in self.favoritos:
            conteudo += f'\n:video_game: [blue]{game}[/]'
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

j1 = Gamer('Fabricio da Silva', "detonator2025")
j1.add_favoritos('Mario Bros')
j1.add_favoritos('Sonic')
j1.add_favoritos('God of War')
j1.add_favoritos('Fortnite')
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Call of Duty')
j2.ficha()