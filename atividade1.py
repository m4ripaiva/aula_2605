class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")

aluno1 = Aluno("João Silva", "12345", "Engenharia")
aluno2 = Aluno("Maria Souza", "67890", "Medicina")

aluno1.exibir_dados()
print("-" * 20)
aluno2.exibir_dados()