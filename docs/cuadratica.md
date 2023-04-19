# Función cuadratica

La función cuadrática representa una parábola que puede tener uno o dos puntos de intersección con el eje x.

## Argumentos

- `a`: Un numero expresado algebraicamente con el valor a
- `b`: Un numero expresado algebraicamente con el valor b
- `c`: Un numero expresado algebraicamente con el valor c

## Valor de retorno

Las dos soluciones son las intersecciones de la ecuación con el eje x, es decir, los puntos donde la curva cruza el eje x.

## Excepciones

- `ValueError`: Si el argumento `a` es igual a 0

## Ejemplos

```python
>>> from matematicassimple import cuadratica
>>> cuadratica(a=8, b=6, c=9)
((-0.375+0.9921567416492215j), (-0.375-0.9921567416492215j))
>>> cuadratica(a=1, b=-10, c=25)
(5.0, 5.0)
```

## Referencias

::: matematicassimple.cuadratica