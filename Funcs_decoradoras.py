"""
Funções Decoradoras

Primeiro exemplo, decora um função simples de exibir o nome depois adiciona um sobrenome
"""
def decoradora(funcao):
    def interna(nome):
        nome_alterado = nome + " Oliveira"
        return funcao(nome_alterado)

    return interna


def exibir_nome(nome):
    print(nome)

#função normal
exibir_nome('Thiago')

#criando função decoradora
decorada = decoradora(exibir_nome)

#função decoradora com sobrenome
decorada('Thiago')
decorada('Marcos')

"""
Funções Decoradoras com paramatros

Decora uma função, mas é possivel passar um argumento
"""

#criando a decoradora com parametros
def decoradora(funcao, multiplicador):
    def interna(numero):
        return funcao(multiplicador, numero)
    
    return interna

#função que vai ser decorada
def multiplicar(multiplicador, numero):
    return multiplicador * numero

#cria a decorada com o multiplicador padrão
decorada = decoradora(multiplicar, 10)

print(decorada(5))


"""
Decorators
"""

def decoradora_2(funcao):
    def interna(nome):
        print(*nome, sep='-')
        funcao(nome)

    return interna

@decoradora_2
def exibir_nome(nome):
    print(nome)

exibir_nome('Thiago')