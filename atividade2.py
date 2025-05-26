class Aluno:
    def __init__(self, nome, turma, nota):
        self.nome = nome
        self.turma = turma
        self.nota = nota

aluno1 = Aluno("Carlos", "Turma A", 8.5)
aluno2 = Aluno("Ana", "Turma B", 9.0)

print(f"Aluno 1: {aluno1.nome}, {aluno1.turma}, Nota: {aluno1.nota}")
print(f"Aluno 2: {aluno2.nome}, {aluno2.turma}, Nota: {aluno2.nota}")
