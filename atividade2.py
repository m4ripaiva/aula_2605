class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")
        print("-" * 20)  

aluno1 = Aluno("rian", "53421", "Matemática")
aluno2 = Aluno("yasmin", "67890", "Direito")

aluno1.exibir_dados()
aluno2.exibir_dados()
