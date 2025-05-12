# Classificacao de list com sort()
# Objetos de lista têm um método sort() que classificará a lista alfanumericamente, em ordem crescente, por padrão:

#Classifique a lista alfabeticamente:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Classifique a lista numericamente:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Ordenar em ordem decrescente
# Para classificar em ordem decrescente, use o argumento de palavra-chave reverse = True:

# Classifique a lista alfabeticamente em ordem decrescente:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Classifique a lista numericamente em ordem decrescente:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist


# Classificação sem distinção entre maiúsculas e minúsculas
# Por padrão, o método sort() diferencia maiúsculas de minúsculas, resultando em todas as letras maiúsculas sendo classificadas antes das minúsculas:

# Execute uma classificação da lista que não diferencia maiúsculas de minúsculas:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Ordem reversa
# O método reverse() inverte a ordem de classificação atual dos elementos.

# Inverta a ordem dos itens da lista:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

