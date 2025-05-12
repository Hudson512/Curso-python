# Inserir um novo intem em uma posição na lista

thislist1 = ["apple", "banana", "cherry"]
thislist1.insert(2, "watermelon")
print(thislist1)
print()

# Adicionar um item ao final da lista
thislist2 = ["apple", "banana", "cherry"]
thislist2.append("orange")
print(thislist2)
print()

#  acrescentar elementos de outra lista à lista atual

thislist3 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist3.extend(tropical)
print(thislist3)
print()

# remover um item especifico na lista.
# Obs: Se houver mais de um item com o valor especificado, o método remove() remove a primeira ocorrência

thislist = ["apple", "banana", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
print()

# Remover índice especificado
# obs: Se você não especificar o índice, o método pop() removerá o último item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
print()

# Limpar a lista
# obs: A lista ainda permanece, mas não tem conteúdo.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
print()

# deletar a lista
# obs: O lista é excluida completamente (free).
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist) # Error