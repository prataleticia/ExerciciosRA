# exercicio 1 SLIDE 5
a = []
i = 0
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    a.append(num)

# exercicio 2 SLIDE 5

a = []
i = 0
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    a.append(num)

print(f"\nOs 10 números inteiros digitados foram: ")
for numeros in a:
    print(numeros)

# exercicio 3 SLIDE 5
a = []
i = 0

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    a.append(num)

print(f"\nOs valores registrados são: ")
print(a)

valor_max = max(a)
valor_min = min(a)

print(f"\nO maior valor da lista é: {valor_max}")
print(f"\nO menor valor da lista é: {valor_min}")

# exercicio 4 SLIDE 5

quantidade = int(input("Digite a quantidade de alunos da turma (max 100): "))
notas_alunos = []
abaixo = []
acima = []
i = 0

for i in range (quantidade):
    nota = int(input(f"Digite a nota do {i + 1}º aluno: "))
    notas_alunos.append(nota)
    i = i+1

    if nota < 60:
        abaixo.append(nota)
    elif nota >= 60:
        acima.append(nota)

print("\nAs notas registradas foram: ")
for notas in notas_alunos:
    print(notas)

print("\nA quantidade de alunos acima da média são: ")
print(len(acima))

print("\nA quantidade de alunos abaixo da média são: ")
print(len(abaixo))

# exercicio 5 SLIDE 5
num = []
par = []
impar = []
i = 0

for i in range(5):
    numeros = int(input(f"Digite o {i + 1}º número inteiro: "))
    num.append(numeros)

    if numeros % 2 == 0:
        par.append(numeros)
    elif numeros % 2 == 1:
        impar.append(numeros)
    else:
        print("O número digitado não se enquadra em ímpar ou par")

print(f"\nO maior número par da lista é: ", {max(par)})
print(f"\nO menor número ímpar da lista é: ", {min(impar)})

print(f"\nA soma de todos os elementos da lista é:", sum(num))

media = sum(num) / len(num)
print(f"\nA média dos elementos da lista é: {media:.2f}")