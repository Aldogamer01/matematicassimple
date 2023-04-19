# Función ordenar

Ordena los numeros de una lista de menor a mayor o viceversa

## Argumentos

- `alreves`: True para ordenar de mayor a menor y False para ordenar de menor a mayor
- `numeros`: Una lista en el que contienen los numeros que se van a ordenar

## Valor de retorno

Desc del output

## Excepciones

- `ValueError`: Si el argumento `numeros` esta vacio

## Ejemplos

```python
>>> from matematicassimple import ordenar
>>> ordenar(alreves=False, numeros=[4,1,0,9,32,51,6,2,8,43])
[0, 1, 2, 4, 6, 8, 9, 32, 43, 51]
>>> ordenar(alreves=True, numeros=[4,1,0,9,32,51,6,2,8,43])
[51, 43, 32, 9, 8, 6, 4, 2, 1, 0]
```

## Referencias

::: matematicassimple.ordenar