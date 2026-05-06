# EXERCICIO 11

numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print("Este número é múltiplo de 3.")
else:
    print("Este número não é múltiplo de 3.")

#####################################################

# EXERCICIO 12

numero = int(input("Digite um número: "))
if numero >= 10 and numero <= 20:
    print("Este número está entre 10 e 20")
else:
    print("Este número não está entre 10 e 20")

####################################################

#EXERCICIO 13

idade = int(input("Digite sua idade: "))
if idade <= 17:
    print("Você é menor de idade!")
elif idade >= 18 and idade <= 65:
    print("Você é adulto!")
else:
    print("Você é idoso!")

##################################################

#EXERCICIO 14

numero = int(input("Digite um número e diremos se ele é par e positivo: "))
if numero > 0 and numero % 2 == 0:
    print("O número que você digitou é positivo e par!")
elif numero > 0 and numero % 2 != 0:
    print("O número que você digitou é positivo, mas não é par!")
elif numero < 0 and numero % 2 == 0:
    print("O número que você digitou é par, mas não é positivo!")
elif numero < 0 and numero % 2 != 0:
    print("O número que você digitou não é positivo e não é par!")
else:
    print("O número que você digitou é zero!")

#################################################

#EXERCICIO 15

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == n2 == n3:
    print("Os três números são iguais!")
elif n1 != n2 != n3 != n1:
    print("Os três números são diferentes!")
elif n1 == n2 != n3 or n1 == n3 != n2 or n2 == n3 != n1 :
    print("Somente dois números são iguais!")

###################################################

#EXERCICIO 16

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
if n1 > n2:
    print(f"O número {n1} é maior que {n2}.")
elif n1 < n2:
    print(f"O número {n1} é menor que {n2}.")
elif n1 == n2:
    print("Os números digitados são iguais!")

##################################################

#EXERCICIO 17

temp = int(input("Digite a temperatura em graus celcius: "))
if temp < 15:
    print("A temperatura está fria!")
elif temp >= 15 and temp <= 30:
    print("A temperatura está agradável!")
else:
    print("A temperatura está quente!")

#################################################

#EXERCICIO 18

email = str(input("Digite seu email: "))
senha = str(input("Digite sua senha: "))

if email != "" or senha != "":
    print("Acesso liberado!")
else:
    print("Acesso bloqueado!")

################################################

#EXERCICIO 19

valor = float(input("Digite o valor e diremos se ele está sujeito a desconto: "))

desconto1 = valor * 10/100
desconto2 = valor * 20/100
sub1 = valor - desconto1
sub2 = valor - desconto2

if valor >= 100 and valor <= 199:
    print("Parabéns, você recebeu um desconto de 10%!")
    print("O valor total a ser pago será de: ", sub1)
elif valor >=200:
    print("Parabéns, você recebeu um desconto de 20%!")
    print("O valor total a ser pago será de: ", sub2)
else:
    print("Que pena! Você não recebeu nenhum desconto!")

##################################################

#EXERCICIO 20

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"O número {n1} é maior!")
elif n2 > n1 and n2 > n3:
    print(f"O número {n2} é maior!")
elif n3 > n1 and n3 > n2:
    print(f"O número {n3} é maior!")
elif n1 == n2 == n3:
    print("Os três números são iguais!")
elif n1 == n2 and n2 > n3:
    print(f"O número {n1} é maior!")
elif n1 == n3 and n3 > n2:
    print(f"O número {n1} é maior!")
elif n2 == n3 and n3 > n1:
    print(f"O número {n2} é maior!")

#####################################################

# EXERCICIO 21

soma = 0

limite = int(input("Digite um número de limite da soma: "))
for i in range(1, limite + 1):
    soma += i
print(f"A soma dos números de 1 até {limite} é: {soma}")

####################################################

# EXERCICIO 22

valor = int(input("Digite o valor limite (20): "))
for numeros in range(1, valor+1):
    if numeros % 2 == 0:
       print(numeros)

#####################################################

# EXERCICIO 23

soma = 0

for i in range(5):
    valor = int(input("Digite um valor inteiro: "))
    soma = soma + valor
media = soma / 5
print(media)

#####################################################

#EXERCICIO 24

contador = 0

while True:
    numero = int(input("Digite um numero: "))
    if numero < 0:
      contador = contador + 1
      print(f"Total de números negativos digitados: {contador}")


#######################################################
