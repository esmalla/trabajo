lista1=['Uvas','Peras','Manzanas','Mangos']

print(lista1)

print(lista1[1])  #imprime el elemento x de la lista


for fruta in lista1:#for donde el ciclo es fruta en lista 1
    print(fruta)

hayFruta="kiwi" in lista1 #busca x en la lista
print(hayFruta)

lista1.append("kiwi")  #agrega un elememto al final de la lista
print(lista1)
print(len(lista1)) #Tamaño d elementos en la lista

lista1.insert(0,"sandia")

print(lista1)


lista1[2]="Piña" # remplaza el elmento dos por x

lista1.remove("kiwi") #borra el elemento x

print(lista1)

lista1.pop()#borra el ultimo elemento de la lista
print(lista1)

lista1.pop(0)

print(lista1)


lista1.sort() #ordena los elementos de la lista




lista2= lista1.copy()#copia una lista a otra

lista2.reverse()# coloca los elementos de la lista a la inversa


print(lista1)
print(lista2)

lista1.clear()

