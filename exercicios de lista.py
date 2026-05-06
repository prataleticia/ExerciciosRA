# escreva um programa que registre o nome dos alunos de uma turma de 3 alunos

nomes_alunos = []

for i in range (3):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nomes_alunos.append(nome)
print("\nNome dos alunos registrados: ")
for nomes in nomes_alunos:
    print(nomes)