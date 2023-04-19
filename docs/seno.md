# Función seno

Función trigonométrica que relaciona el ángulo de un triángulo rectángulo con la razón entre el cateto opuesto y la hipotenusa

## Argumentos

- `numero`: El numero del que se desea obtener su seno
- `repeticiones`: Cuantas veces se repetira para obtener el valor aproximado

## Valor de retorno

El seno del numero ingresado

## Excepciones

- `ValueError`: Si el argumento `repeticiones` es menor o igual a 2

## Ejemplos

```python
>>> from matematicassimple import seno
>>> seno(numero=8, repeticiones=100)
0.9893582466234029
>>> seno(numero=14, repeticiones=1000)
0.9906073556973417
```

## Referencias

::: matematicassimple.seno