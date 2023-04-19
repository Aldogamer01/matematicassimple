def leibniz(repeticiones: int) -> float:
    """
    Para obtener pi de una forma distinta,
    puede usar la formula de leibniz.

    Para eso puede hacer lo siguiente:


    from matematicassimple import leibniz

    leibniz(repeticiones=1000)
    """
    if repeticiones <= 0:
        raise ValueError("Ingrese numeros positivos mayor a 0")
    count = 1
    signo = '-'
    divisor = 3
    for i in range(repeticiones):
        if signo == '-':
            count = count - 1/divisor
            divisor = divisor + 2
            signo = '+'
        else:
            count = count + 1/divisor
            divisor = divisor + 2
            signo = '-'
    return 4*count