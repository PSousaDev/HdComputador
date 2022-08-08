class Computador:
    def __init__(self,modelo,fabricante,processador,memóriaRAM,tamanhoDoHd,espacoOcupadoDoHd,estaligado):
        self.modelo = modelo
        self.fabricante =fabricante
        self.processador = processador
        self.memóriaRAM = memóriaRAM
        self.tamanhoDoHd = float(tamanhoDoHd)
        self.espacoOcupadoDoHd = float(espacoOcupadoDoHd)
        self.estaligado =estaligado
        self.valor=0
def liga(self):
    self.estaligado=self.estaligado
    print("computador esta ligado")
def desliga(self):
    self.estaligado=self.estaligado
    print("computador esta desligado")
def limpahd(self):
    if self.tamanhoDoHd>=float(self.valor) and self.espacoOcupadoDoHd>=1:
        self.espacoOcupadoDoHd=self.espacoOcupadoDoHd-float(self.valor)
        print('voce tem :',self.espacoOcupadoDoHd,'GB','ocupados do hd ')
        print('voce limpou :',self.valor,'GB','do hd ')

    else:
        print("computador não tem esta quantidade de espaco ocupado")
def ocuparhd(self):
    if self.tamanhoDoHd>=float(self.valor) and float(self.espacoOcupadoDoHd)>=0:
        self.espacoOcupadoDoHd=self.espacoOcupadoDoHd+float(self.valor)
        print('voce tem :',self.espacoOcupadoDoHd,'ocupados do hd ')
        print('voce adicionou :',self.valor,'GB','no hd ')
    else:
        print("sem espaco no hd")
