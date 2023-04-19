# Función raiz

Obtiene la raiz de un numero

## Argumentos

- `al`: Para decir cuantas veces se obtendra su raiz
- `numero`: Para decir que numero se obtendra su raiz

## Valor de retorno

El resultado de la operacion.

## Excepciones

- `ValueError`: Si el argumento `numero` es menor a 0
- `ValueError`: Si el argumento `al` es menor a 1

## Ejemplos

```python
>>> from matematicassimple import raiz 
>>> raiz(al=2, numero=8)
2.8284271247461903
>>> raiz(al=3, numero=81)
3
```

## Referencias

::: matematicassimple.raiz