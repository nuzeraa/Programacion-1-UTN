#primero creamos la lista compras

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#agregamos "jugo" a la tercer lista

compras[2].append ("jugo")

#reemplazamos "fideos" por "tallarines" en segunda lista

compras[1][1] = "tallarines"

#eliminamos pan de la primer lista

compras[0].remove ("pan")

#imprimimos la lista actualizada

print("la lista actualizada es:", compras)