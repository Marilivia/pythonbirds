class Pessoa:
    olhos = 2 #atributo de classe
    def __init__(self, *filhos, nome=None,idade = 0):
        #atributos de instancia
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa (nome = 'Renzo',idade=40)
    carlos = Pessoa(nome='Carlos',idade=23)
    luciano = Pessoa(renzo ,carlos,nome='Luciano')
    for filho in luciano.filhos:
        print(filho.nome, filho.idade)


    luciano.sobrenome = 'Ramalho'
    print(luciano.nome)
    print(luciano.idade)
    print(luciano.filhos)
    print(Pessoa.olhos)
    print(luciano.olhos)

