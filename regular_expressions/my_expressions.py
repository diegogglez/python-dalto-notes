import re

#* detectando un numero CABA y ocultándolo

text = 'Hola Pedro, mi número es: +54 11 4421-4532'

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

text_replaced = re.sub(pattern, '(número oculto)', text)

print(text_replaced)