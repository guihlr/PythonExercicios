def divisores(n):
    lista = list()
    for i in range(1, n + 1):
        if n % 1 == 0:
            lista.append(i)
    return lista

def primo(n):
    div = len(divisores(n))
    if div == 2:
        return True
    return False

