import math
print(math.factorial(6))



#--------------------Trabalhando com Dicionários----------------#
print('\n\n')
print("-------------Trabalhando com Dicionários--------------")
classe = {"Ana": 4.5,
         "Beatriz": 6.5,
          "Geraldo": 10.0,
          "José": 1.0,
          "Maria": 9.5}
notas = classe.values()
média = sum(notas)/5
print("A Média da classe é ",média)

print('\n======================================================')
dic = {"Salgado":4.50,
       "Lanche":6.50,
       "Suco": 3.00,
       "Refrigerante": 3.50,
       "Doce": 1.00}

print(dic)
print('\n======================================================')
D = {"arroz":17.30,"feijão":12.50,"carne":23.90,"alface":3.40}
print(D)

D["carne"] = 25.0
D["tomate"] = 8.80
print(D)


#--------------------Praticando com Tuplas-------------------#
print('\n\n')
print("----------------Praticando com Tuplas-----------------")
T = (10,20,30,40,50)
a,b,c,d,e = T
print("a =",a,"b =",b)

print("d + e =",d+e)
#-----------------Praticando com Listas---------------------#
print('\n\n')
print("----------------Praticando com Listas-----------------")
L = [5,7,2,9,4,1,3]
print("Lista = ",L)
print("O tamanho da lista é ",len(L))
print("O Maior elemento da lista é ",max(L))
print("O Menor elemento da lista é ",min(L))
print("A Soma dos elementos da lista é ",sum(L))
L.sort()
print("Lista em ordem crescente: ",L)
L.reverse()
print("Lista em ordem decrescente: ",L)