class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

motor = Motor()
velocidade = motor.velocidade
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)

NORTE = 'Norte'
LESTE = 'Leste'
SUL = 'Sul'
OESTE = 'Oeste'

class Direcao:

    # rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    # def girar_a_direita (self)
    # self.valor=self.rotacao_a_direita_dct[self.valor]

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita (self):
        if self.valor == NORTE:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE

    def girar_a_esquerda (self):
        if self.valor == NORTE:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = NORTE

direcao = Direcao()
print(direcao.valor)
direcao.girar_a_direita()
print(direcao.valor)
direcao.girar_a_esquerda()
print(direcao.valor)

class Carro:
    def __init__(direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
         return self.motor.velocidade
    def calcular_direcao(self):
        return self.direcao.valor

    def acelerar(self):
        self.motor.acelerar()
    def frear(self):
        self.motor.frear()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()



