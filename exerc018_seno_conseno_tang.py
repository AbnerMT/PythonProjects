from math import sin, acos, atan, radians
angu = float(input('Digite o anguloº: '))
seno = sin(radians(angu))
conseno = acos(radians(angu))
tangente = atan(radians(angu))
print(f' O angulo de {angu} tem o Seno : {seno:.2f}\n O angulo de {angu} tem o Conseno {conseno:.2f}\n O angulo de {angu} tem a Tangente {tangente:.2f}')
