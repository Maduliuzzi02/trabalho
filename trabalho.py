class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
        self.frequencia = 0

    def adicionar_notas(self, notas):
        if len(self.notas) + len(notas) <= 4:
            self.notas.extend(notas)
        else:
            print("O aluno pode ter no máximo 4 notas.")

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

    def adicionar_frequencia(self, frequencia):
        self.frequencia = frequencia

    def calcular_situacao(self, carga_horaria):
        frequencia_percentual = (self.frequencia / carga_horaria) * 100
        media = self.calcular_media()

        if frequencia_percentual < 75:
            return "Reprovado por Falta"
        elif media >= 7:
            return "Aprovado"
        else:
            return "Reprovado por Nota"


class Sistema:
    def __init__(self):
        self.alunos = []
        self.carga_horaria = 0

    def definir_carga_horaria(self):
        self.carga_horaria = int(input("Digite a carga horária da disciplina: "))

    def adicionar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        self.alunos.append(Aluno(nome))

    def editar_nome_aluno(self):
        nome_atual = input("Digite o nome atual do aluno: ")
        aluno = self.encontrar_aluno(nome_atual)
        if aluno:
            novo_nome = input("Digite o novo nome do aluno: ")
            aluno.nome = novo_nome
        else:
            print("Aluno não encontrado.")

    def remover_aluno(self):
        nome = input("Digite o nome do aluno a ser removido: ")
        aluno = self.encontrar_aluno(nome)
        if aluno:
            self.alunos.remove(aluno)
        else:
            print("Aluno não encontrado.")

    def adicionar_notas_aluno(self):
        nome = input("Digite o nome do aluno: ")
        aluno = self.encontrar_aluno(nome)
        if aluno:
            notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
            aluno.adicionar_notas(notas)
        else:
            print("Aluno não encontrado.")

    def adicionar_frequencia_aluno(self):
        nome = input("Digite o nome do aluno: ")
        aluno = self.encontrar_aluno(nome)
        if aluno:
            frequencia = int(input("Digite a frequência do aluno (número de aulas assistidas): "))
            aluno.adicionar_frequencia(frequencia)
        else:
            print("Aluno não encontrado.")

    def imprimir_relatorio_geral(self):
        if not self.carga_horaria:
            print("Defina a carga horária antes de gerar o relatório.")
            return

        for i, aluno in enumerate(self.alunos, start=1):
            situacao = aluno.calcular_situacao(self.carga_horaria)
            print(f"{i}. {aluno.nome} - nota: {aluno.calcular_media():.1f} / frequência: {aluno.frequencia} aulas - ({situacao})")

    def imprimir_relatorio_por_situacao(self):
        if not self.carga_horaria:
            print("Defina a carga horária antes de gerar o relatório.")
            return

        situacao_filtro = input("Digite a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
        for i, aluno in enumerate(self.alunos, start=1):
            situacao = aluno.calcular_situacao(self.carga_horaria)
            if situacao == situacao_filtro:
                print(f"{i}. {aluno.nome} - nota: {aluno.calcular_media():.1f} / frequência: {aluno.frequencia} aulas - ({situacao})")

    def encontrar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
                return aluno
        return None


def main():
    sistema = Sistema()
    sistema.definir_carga_horaria()

    while True:
        print("\n1. Adicionar Aluno")
        print("2. Editar Nome do Aluno")
        print("3. Remover Aluno")
        print("4. Adicionar Notas ao Aluno")
        print("5. Adicionar Frequência ao Aluno")
        print("6. Imprimir Relatório Geral")
        print("7. Imprimir Relatório por Situação")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sistema.adicionar_aluno()
        elif opcao == "2":
            sistema.editar_nome_aluno()
        elif opcao == "3":
            sistema.remover_aluno()
        elif opcao == "4":
            sistema.adicionar_notas_aluno()
        elif opcao == "5":
            sistema.adicionar_frequencia_aluno()
        elif opcao == "6":
            sistema.imprimir_relatorio_geral()
        elif opcao == "7":
            sistema.imprimir_relatorio_por_situacao()
        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
