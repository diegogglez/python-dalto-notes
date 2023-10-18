# En matemática, la sucesión de Fibonacci se trata de una serie infinita de números naturales que empieza con un 0 y un 1
# y continúa añadiendo números que son la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233...
#* Escribir un programa que calcule la serie de fibonacci entre 0 y el número dado

def fibonacci(num):
  a, b = 0, 1
  fibonacci_list = [0]
  for i in range(num):
    if b > num: return fibonacci_list
    else: 
      fibonacci_list.append(b)
      a, b = b, a + b

result = fibonacci(30)
print(result) # [0, 1, 1, 2, 3, 5, 8, 13, 21]   