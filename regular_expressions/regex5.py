import re

text = 'Este es un ejemplo de una url: https://www.example.com y también podemos '

# el signo de ? hace que lo que tenga a la izquierda no sea requerido solo mostrará 0 o 1 coincidencia
pattern = 'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern, text)

print(result)