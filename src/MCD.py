def maximo_comun_divisor(a: int, b:int) -> int :
    """
    Para obtener el maximo comun divisor
    de 2 numeros, solo use el siguiente
    codigo de ejemplo:


    from matematicassimple import MCD

    MCD(a=18, b=12)
    """
    if a <= 0 or b <= 0:
        raise ValueError("Ingrese un valor mayor a 0")
    lista1 = []
    lista2 = []
    res = 1
    if a == b:
        return a
    elif a == 1 or b == 1:
        return 1
    else:
        for i in range(a):
            if a/(a-i) == int(a/(a-i)):
                lista1.append(a/(a-i))
        for i in range(b):
            if b/(b-i) == int(b/(b-i)):
                lista2.append(b/(b-i))
        for i in range(len(lista1)):
            for ii in range(len(lista2)):
                if lista1[i] == lista2[ii]:
                    res = lista1[i]
                    break
        return res