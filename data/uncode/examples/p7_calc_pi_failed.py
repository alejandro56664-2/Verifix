### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 7-10 líneas de código)

# Entrada del programa (~ 1 línea).
n = int(input())                      

# Serie de Leibniz (~ 5-8 líneas). 
def dataset1_p7_calc_pi_success(n):
  pi = 0

  for i in range(0,x):
    numerador =  ((-1)**i)
    denominador = ((2*i)+1)
    pi += numerador / denominador

  print(f'{pi*4: .10f}')