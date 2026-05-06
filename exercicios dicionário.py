# exercicio 1
infos = {"nome": "Letícia", "idade": "21", "cidade": "Curitiba"}
chaves = input("Informe a info desejada: ")
if chaves in infos:
    print(infos[chaves])
else:
    print("Chave não encontrada!")
