import cmath
from .raiz import raiz
from .elevado import elevado
def cuadratica(a: float,b: float,c: float) -> float:
    """
    Una función cuadrática es una función que puede ser descrita por una ecuación de la forma y = ax2 + bx + c, donde a ≠ 0
    """
    if a == 0:
        raise ValueError("El valor \"a\" no puede ser igual a 0")
    discriminante = elevado(al=2, numero=b)-4*a*c
    if discriminante >= 0:
        return (-b + raiz(2, discriminante))/(2*a), (-b - raiz(2, discriminante))/(2*a) 
    else:
        return (-b + cmath.sqrt(discriminante))/(2*a), (-b - cmath.sqrt(discriminante))/(2*a) 