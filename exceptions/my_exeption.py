class MyException(Exception):
  def __init__(self, err):
    print(f'Impresionante, cometiste el siguiente error: {err}')
   
#* Lanzando mi propia excepcion:
# raise MyException('jajaja, persona poco culta')
 
#* Manejandola
try:
  raise MyException('jajaja, persona poco culta')
except:
  print('Como vas a cometer ese error?')
