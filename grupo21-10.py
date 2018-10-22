def mensagem(msg):
    n = input(msg)
    return n


def soma(n1, n2):
    resultado = n1 + n2
    return resultado


def Main():
    texto = mensagem("Digite seu nome:")
    primeiroNumero = 10
    segundoNumero = 20
    somaDeDoisNumeros = soma(primeiroNumero, segundoNumero)
    print(somaDeDoisNumeros)


Main()
