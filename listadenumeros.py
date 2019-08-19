listas = [1,2,3,4,5,6,7,8,9,0]

def par(listas):
    for lista in listas:
        if lista % 2 == 0:
            print(lista)

def impar(listas):
    for lista in listas:
        if lista % 2 != 0:
            print (lista)

par(listas)
impar(listas)




