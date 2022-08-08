
from turtle import up
from computador import Computador, desliga, liga, limpahd, ocuparhd
print("----------------------------------------------------------------")
modeloc1=input("digite o modelo do seu computador""\n")
fabricantec1=input("digite seu fabricante""\n")
processadorc1=input("digite seu processador""\n")
memoriaramc1=int(input("digite a quantidade de  memoria""\n"))
tamanhohdc1=float(input("digite seu espaco do disco no computador""\n"))
espacoocupado=float(input("digite seu espaco ocupado no computador""\n"))
ligar=input("voce deseja ligar o computador(S/N)""\n")
c1=Computador(modeloc1,fabricantec1,processadorc1,memoriaramc1,tamanhohdc1,espacoocupado,ligar)
if ligar=='S'or 's':
    liga(c1)
elif ligar=='N'or 'n':
    desliga(c1)
while(True):
    print("\n""================================")
    print("digite a opcao que deseja""\n")
    print("(1)-Para ocupar o disco""\n")
    print("(2)-Para liberar espaco no disco""\n")
    opcao=input()
    if(opcao=="1"):
        c1.valor=input("digite o tamanho do espaco que deseja ocupar o disco""\n")
        ocuparhd(c1)
    elif(opcao=="2"):
        c1.valor=input("digite o tamanho do espaco que deseja limpar o disco""\n")
        limpahd(c1)
    print("Deseja Continuar?(S/N)")
    opcaoContinuar=input()
    if opcaoContinuar.upper()=='N':
        break
