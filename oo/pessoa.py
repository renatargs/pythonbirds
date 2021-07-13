class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    renata = Pessoa(nome='Renata')
    erick = Pessoa(renata,nome='Erick')
    print(Pessoa.cumprimentar(erick))
    print(id(erick))
    print(erick.cumprimentar())
    print(erick.nome)
    print(erick.idade)
    for filho in erick.filhos:
        print(filho.nome)
    erick.sobrenome = 'Quinteiro'
    del erick.filhos
    print(erick.__dict__)
    print(renata.__dict__)
