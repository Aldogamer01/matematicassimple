# Función temperatura

Cambia los Celsius a Fahrenheit o viceversa

## Argumentos

- `conversion`: El tipo de conversion que se quiere realizar, 1 para convertir Celsius a Fahrenheit y 2 para viceversa
- `grados`: Los grados que se desean convertir

## Valor de retorno

La temperatura convertida a su otra conversion

## Excepciones

- `ValueError`: Si la `argumento` no es valida

## Ejemplos

```python
>>> from matematicassimple import temperatura
>>> temperatura(conversion=1, grados=36.8)
98.24
>>> temperatura(conversion=2, grados=85.5)
29.72222222222222
```

## Referencias

::: matematicassimple.ChangeTemperature