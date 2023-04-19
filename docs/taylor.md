# Función taylor

Calcula la serie de Taylor para la función exponencial.

## Argumentos

- `repeticiones`: El número de términos que se quieren sumar. Debe ser un número entero mayor a cero.

## Valor de retorno

Un número real que representa el valor aproximado de la serie de Taylor para la función exponencial.

## Excepciones

- `ValueError`: Si el argumento `repeticiones` es menor o igual a cero.

## Ejemplos

```python
>>> from matematicassimple import taylor
>>> taylor(10)
3.828968253968254
>>> taylor(100)
6.17737751763962
```

## Referencias

::: matematicassimple.taylor