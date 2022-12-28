distanciametros, velocidadmax, tiemposegundos = input().split()
distanciametros=float(distanciametros)
velocidadmax=float(velocidadmax)
tiemposegundos=float(tiemposegundos)
velocidadconductor=(distanciametros/1000)/(tiemposegundos/3600)
if distanciametros<0 or velocidadmax<0 or tiemposegundos<0:
    print('ERROR')
elif velocidadconductor<velocidadmax:
    print('OK')
elif velocidadconductor>velocidadmax and velocidadconductor<velocidadmax*1.20:
    print('MULTA')
elif velocidadconductor>=velocidadmax*1.20:
    print('CURSO SENSIBILIZACION')