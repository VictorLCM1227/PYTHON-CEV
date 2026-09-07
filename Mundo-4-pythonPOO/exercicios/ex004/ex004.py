class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade,)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = ''
        self.nivel = ''

    def dar_aula(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = ''
        self.setor = ''

    def bater_ponto(self):
        pass


a1 = Aluno('José', 17, 'Informática', 'T01')