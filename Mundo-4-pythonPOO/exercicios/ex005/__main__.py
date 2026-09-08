from rich import inspect
from rich import print
from classesex005 import Aluno, Funcionario, Pessoa, Professor

a1 = Aluno('José', 17, 'Informática', 'T01')
a1.fazer_aniversario()


p1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
a1.fazer_aniversario()
p1.fazer_aniversario()
p1.dar_aula()


f1 = Funcionario('Claudia', 27, 'Secretária', 'Secretaria')
f1.fazer_aniversario()
f1.bater_ponto()