# Función fibonacci

Secuencia obtenida sumando el numero anterior con el actual

## Argumentos

- `repeticiones`: Cuantas veces se quiere repetir la secuencia

## Valor de retorno

Una secuencia fibonacci

## Excepciones

- `ValueError`: Si el argumento `repeticiones` es menor o igual a 0

## Ejemplos

```python
>>> from matematicassimple import fibonacci
>>> fibonacci(repeticiones=10)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
>>> fibonacci(repeticiones=25)
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025]
```

## Referencias

::: matematicassimple.fibonacci