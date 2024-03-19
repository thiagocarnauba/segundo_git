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