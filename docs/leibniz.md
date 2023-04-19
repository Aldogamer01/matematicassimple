# Función leibniz

Una formula inventada por Leibniz que obtiene el valor de pi

## Argumentos

- `repeticiones`: Cuantas veces se repetira el proceso para obtener el valor aproximado a pi

## Valor de retorno

Un posible numero aproximado a pi

## Excepciones

- `ValueError`: Si el argumento `repeticiones` es menor o igual a 0

## Ejemplos

```python
>>> from matematicassimple import leibniz
>>> leibniz(repeticiones=1000)
3.1425916543395442
>>> leibniz(repeticiones=10000)
3.1416926435905346
```

## Referencias

::: matematicassimple.leibniz