# Exercicio 31

lista = [1, 2, 3, 4, 5]
print(sum(lista))

# Exercicio 32

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for elementos in lista2:
    if elementos % 2 == 0:
        pares.append(elementos)

print(len(pares))

# Exercicio 33

notas = {"Pedro": 84,
         "João": 76,
         "Igor": 100}
print(notas)

# Exercicio 34

lista4 = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Digite o número que deseja saber se está na lista: "))
if num in lista4:
    print("O número digitado está na lista!")
else:
    print("O número digitado não está na lista!")

# Exercicio 35

lista5 = [1, 23, 4, 6, 24, 65, 5, 76, 2, 7]
maior = []

for elemento in lista5:
    if elemento > 10:
        maior.append(elemento)

print(maior)

# Exercicio 36

produtos = {"Oreo": 15.00,
         "Doritos": 20.00,
         "Cini": 6.00}
print("\nProdutos e valores atuais :")
print(produtos)

att = input("Deseja atualizar o valor de um produto? (sim/não): ")
if att == "sim":
    chave = input("Qual produto deseja alterar?")
    if chave in produtos:
        valor = float(input("Digite o novo valor: "))
        produtos[chave] = valor
        print("\nProduto atualizado com sucesso!")
        print(produtos)
    else:
        print("Produto não encontrado!")
else:
    print("Sessão finalizada!")

# Exercicio 37

lista7 = [23,45,78,90,64,221,454,343]
media = sum(lista7)/len(lista7)

print(media)

# Exercicio 38

lista8 = [1,-1,2,-2,3,-3,4,-4,5,-5]
for elementos in lista8:
    if elementos < 0:
        lista8.remove(elementos)

print(lista8)

# Exercicio 39

nomes = []

while True:
    nome = input("Digite o nome que deseja armazenar: ")
    if nome == "fim":
        break
    nomes.append(nome)

print(nomes)

# Exercicio 40
dados = {
    "nome": "lele",
    "cidade": "curitiba"
}

print("idade" in dados)

# Exercicio 41

lista11 = [1,1,1,1,3,3,4,5,6,7,65,4,3,2,11]
print(lista11.count(1))

# Exercicio 42

lista12 = [1,2,3,4,5,6,7,8,9]
print(max(lista12))

# Exercicio 43

produtos = {"Oreo": 15.00,
            "Doritos": 20.00,
            "Cini": 6.00
}

produtos = {k: v * 0.9 for k, v in produtos.items()}
print(produtos)

# Exercicio 44

lista14 = [1,2,3,4,5,6,7,8,9,10,11]
impares = []

for elementos in lista14:
    if elementos % 2 == 1:
        impares.append(elementos)

print(sum(impares))

# Exercicio 45

lista15 = [1,2,3,4,5]
lista_invertida = lista15[::-1]
print(lista_invertida)

# Exercicio 46
import numpy as np

matriz = np.array([[1,2],
                   [3,4]])
print(matriz)

# Exercicio 47

import numpy as np

matriz = np.array([[1,2],
                   [3,4]])
print(np.sum(matriz))

# Exercicio 48
import numpy as np

matriz2 = np.array([
    [1,2,3],
    [6,7,8],
    [11,12,13]
])

print(np.diag(matriz2))

# Exercicio 49
import numpy as np

matriz3 = np.array([
    [1,2,3],
    [6,7,8],
    [11,12,13]
])
k = 2
print(matriz3 * k)

# Exercicio 50
import numpy as np

matriz = np.array([[1,2],
                   [3,4]])
matriz3 = np.array([[4,6],
                   [8,9]])

print(matriz + matriz3)