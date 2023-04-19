# Función CAYP (Calcular area y perimetro)

Calcula el area y perimetro de un poligono regular

## Argumentos

- `figura`: Describe que poligono regular se va a calcular
- `AP`: Elije si calcular el area o el perimetro (1: Area, 2: Perimetro)
- `lado`: Describe la medida de un lado
- `lado2`: Describe la medida del 2do lado 
- `lado3`: Describe la medida del 3er lado
- `radio`: O tambien la apotema sirve para calcular el circulo o los poligonos de 5 o mas lados

## Valor de retorno

La medida del Area o el Perimetro en centimetros

## Excepciones

- `ValueError`: Si el argumento `lado2` en el rectangulo no es valido o no fue obtenido
- `ValueError`: Si el argumento `radio` en el circulo no es valido o no fue obtenido
- `ValueError`: Si el argumento `apotema` en los poligonos de 5 o mas lados no es valido o no fue obtenido
- `ValueError`: Si la argumento `figura` no coincide con las figuras disponibles

## Ejemplos

```python
>>> from matematicassimple import CAYP
>>> CAYP(figura="circulo", AP=1, radio=73)
16733.06
>>> CAYP(figura="hexagono", AP=2, lado=60)
360
```

## Referencias

::: matematicassimple.CAYP