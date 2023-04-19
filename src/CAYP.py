def CAYP(figura: str, AP: int, lado: int = None, lado2: int = None, lado3: int = None, radio: int = None): 
    """
    Puedes calcular el area y perimetro
    de cualquier poligono regular como
    lo es el cuadrado, rectagono, triangulo,
    circulo, pentagono, hexagono, heptagono,
    octagono, nonagono, decagono y endecagono

    Para calcular el area, en AP inserte 1,
    si desea calcular el perimetro, inserte 2.

    Al calcular cuadrado, rectangulo y triangulo,
    solo debe insertar los lados.

    En el triangulo, si no inserta el valor
    del lado 2 o 3, se tomara el valor
    del lado 1

    Al calcular el circulo,
    solo debe insertar el radio.

    Al calcular cualquier poligono de 5 o mas lados,
    solo inserte el lado y apotema.

    Nota:
    El apotema se contara como el radio.
    """
    figura = figura.lower()
    if figura == 'cuadrado':
        if AP == 1:
            return lado*lado
        else:
            return lado*4
    elif figura == 'rectangulo':
        if lado2 == None:
            raise ValueError("No se obtuvo el valor del lado 2")
        if AP == 1:
            return lado*lado2
        else:
            return lado+lado2*2
    elif figura == 'triangulo':
        if AP == 1:
            return lado*lado2/2
        else:
            if lado2 == None:
                lado2 = lado
            if lado3 == None:
                lado3 = lado
            return lado+lado2+lado3
    elif figura == 'circulo':
        if radio == None:
            raise ValueError("Ocurrio un error al calcular el circulo, no se obtuvo el valor del radio")
        if AP == 1:
            return 3.14*radio*radio
        else:
            return 2*3.14*radio,
    elif figura == 'pentagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*5*radio/2
        else:
            return lado*5
    elif figura == 'hexagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*6*radio/2
        else:
            return lado*6
    elif figura == 'heptagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*7*radio/2
        else:
            return lado*7
    elif figura == 'octagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*8*radio/2
        else:
            return lado*8
    elif figura == 'nonagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*9*radio/2
        else:
            return lado*9
    elif figura == 'decagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*10*radio/2
        else:
            return lado*10
    elif figura == 'endecagono':
        if AP == 1:
            if radio == None:
                raise ValueError("Ocurrio un error al calcular el poligono, no se obtuvo el valor del radio")
            return lado*11*radio/2
        else:
            return lado*11