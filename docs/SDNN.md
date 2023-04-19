# Función SDNN (Suma De Numeros Naturales)

Obtiene el resultado de una suma de numeros naturales desde 0 hasta el valor insertado

## Argumentos

- `numero`: El numero del que se desea obtener su SDNN

## Valor de retorno

La suma de los numeros naturales

## Excepciones

- `ValueError`: Si el argumento `numero` es menor a 0

## Ejemplos

```python
>>> from matematicassimple import SDNN
>>> SDNN(numero=100)
5050
>>> SDNN(numero=1000)
500500
```

## Referencias

::: matematicassimple.SDNN