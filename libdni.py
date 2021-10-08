def calculaLetra(numeroDNI):
 lista = 'RTEQGPYFMDKBNHZSAVJLCXW'
 return lista[numeroDNI%23]
numero = int(input("Introduzca número del DNI"))
print("La letra del Dni es:", calculaLetra(numero))