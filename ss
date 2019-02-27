def divisores(n):
    lista = list()
    for i in range(1, n + 1):
        if n % i == 0:
            lista.append(i)
    return lista


def primo(n):
    div = len(divisores(n))
    if div == 2:
        return True
    return False


def perfeito(n):
    div = divisores(n)
    soma = 0
    for i in div:
        soma += i
    soma -= n
    return soma
