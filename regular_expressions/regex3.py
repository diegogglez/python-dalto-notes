import re

text = 'remplazando todas las vocales por el asterisco'

# Al meter las vocales entre corchetes decimos que busque cada una por separado sin importar el orden
new_text = re.sub('[aeiou]', '*', text)

print(new_text)