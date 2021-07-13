class Pessoa:
    olhos = 2 #atributo default ou atributo de classe - valor fixo
    def __init__(self, *filhos, nome=None, idade=31): #declaração de atributos variáveis
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self): #criação de mensagem personalizada
        return f'Olá {id(self)}'
if __name__ == '__main__': #atribuições de valores com condicional
    renata = Pessoa(nome='Renata')
    erick = Pessoa(renata,nome='Erick')
    print(Pessoa.cumprimentar(erick))
    print(id(erick))
    print(erick.cumprimentar())
    print(erick.nome)
    print(erick.idade)
    for filho in erick.filhos: #printa todos os nomes dentro de filhos
        print(filho.nome)
    erick.sobrenome = 'Quinteiro' #atributo dinâmico - não é boa prática, mas ajuda na alteração de formato para única instância
    del erick.filhos #deleta um atributo
    erick.olhos = 1 #altera o valor de olhos apenas para Erick, e passa a pertencer ao __dict__ e não altera os demais objetos e muda o id para esse objeto
    del erick.olhos #deleta o atributo dinâmico de erick, que passa a responder o atributo de classe pessoa
    print(erick.__dict__) #descreve todos os atributos da classe
    print(renata.__dict__)
    # print(Pessoa.nome) não faz sentido - não tem atributo nome na classe Pessoa - erro
    Pessoa.olhos = 3 #altera o valor de olhos para todas os objetos da classe, exceto o que foi atribuido de forma dinâmica
    print(Pessoa.olhos) #como é um atributo de classe, pode ser acessado pela classe Pessoas
    print(erick.olhos) # o atributo pode ser usado para objetos
    print(renata.olhos)
    print(id(renata.olhos))
    print(id(erick.olhos)) # como o atributo é o mesmo, terá o mesmo id para todos
    print(id(renata.olhos), id(erick.olhos), id(Pessoa.olhos)) #terá o mesmo id, tanto para objeto quanto para classe
    # o __dict__ não possui o atributo de classe, ou seja, olhos, somente os atributos de instância
