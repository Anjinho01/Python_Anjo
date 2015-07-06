t = int(input("Digite a quantidade de alunos na sala :"))
k = int(input("Digite o peso que a sala aguenta :"))
n = 1
soma = 0
while n <= t:
    x = int(input("Digite o peso do %d° aluno:"%n))
    soma = soma + x
    n += 1
if soma > k:
    p = soma - k
    print ("A sala não vai aguentar!O peso tem que diminuir %d quilos!"%p)
else:
    t = k - soma
    if t == 1:
        print ("A sala vai aguentar!E a sala ainda aguenta %d quilo!"%t)
    if t >= 2:
        print ("A sala vai aguentar!E a sala ainda aguenta %d quilos!"%t)
    if t == 0:
        print ("A sala vai aguentar!Mas não aguenta mais peso!")
