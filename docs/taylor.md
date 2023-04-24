# Función taylor

Calcula la serie de Taylor para la función exponencial.

## Argumentos

- `x`: El numero que se usara para calcular la serie de Taylor
- `repeticiones`: El número de términos que se quieren sumar. Debe ser un número entero mayor a cero.

## Valor de retorno

Un número real que representa el valor aproximado de la serie de Taylor para la función exponencial.

## Excepciones

- `ValueError`: Si el argumento `repeticiones` es menor o igual a cero.

## Ejemplos

```python
>>> from matematicassimple import taylor
>>> taylor(1,10)
2.7182815255731922
>>> taylor(2,100)
7.389056098930649
```

## Referencias

::: matematicassimple.taylor