from .factorial import factorial
from .elevado import elevado
def taylor(x : float, repeticiones : int) -> float:
    """
    La serie de Taylor es una aproximación
    de funciones mediante una serie de potencias
    o suma de potencias enteras de polinomios como
    llamados términos de la serie, dicha suma se 
    calcula a partir de las derivadas de la función
    para un determinado valor o punto suficientemente 
    derivable sobre la función y un entorno sobre el cual converja la serie.

    
    Para usar la serie de taylor en python, puede hacer lo siguiente:


    from matematicassimple import taylor

    taylor(repeticiones=1000)
    """
    if repeticiones <= 0:
        raise ValueError("Inserte un valor mayor a 0")
    res = 0
    for i in range(repeticiones):
        if i == 0:
            res = 1
        else:
            res = res + elevado(al= i, numero= x)/factorial(i)
    return res