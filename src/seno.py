from .factorial import factorial
from .elevado import elevado
def seno(numero : float, repeticiones : int) -> float:
    """    
    Para usar el seno de x numero en python, puede hacer lo siguiente:


    from matematicassimple import seno

    seno(numero=65, repeticiones=1000)
    """
    if repeticiones <= 2:
        raise ValueError('Inserte el valor "repeticiones" a un numero mayor a 2')
    signo = '+'
    n = 0
    res = numero
    for i in range(repeticiones):
        if i == 0:
            signo = '-'
            n = 3
        elif signo == '-':
            res = res - elevado(n, numero)/factorial(n)
            n=n+2
            signo = '+'
        else:
            res = res + elevado(n, numero)/factorial(n)
            n=n+2
            signo = '-'
    return res