#crearemos un programa que analize un texto especifico
#el ususario debe ingresar 3 letra a su eleccion
#hay que hacer 5 tipo de analisis

#1 cuantas veces aparece cada letra (recomendamos al macenar las letras en una lista y usar metodos de string para contar lo que necesitamos)
#recordemos que pueden existir mayusculas o minusculas y estas deben aparecer pero en minuscula.

#2 debemos decir al ususario cuantas palabras existen en total en el texto completo 
#(string tiene un metodo para transformar palabras en listas y una funcion que averigua el largo de una lista).

#3 debemos decir cual es la primera letra del texto y cual es la ultima (esto podemos conseguirlo con index).

#4 debemos mostrar un ejemplo de como se veria el texto en orden inverso y unir los elementos con espacios intermedios.

#5 el sistema debe responder si la palabra Python existe dentro del texto.
#(podemos usar los booleanos para verificar si se encuentra y un diccionario para asociar el booleano con un string y asi mostrarlo)

texto = input("Ingresa un texto a eleccion: \n")
texto_en_minusculas = texto.lower()

#aca comenzaremos con la 1ra parte
letras_a_buscar = [] #aca creamos un apendice vacio para posteriormente llenarlo con los input

print("\nIngrese uno a uno un total de 3 caracteres para realizar la busqueda:\n")
letras_a_buscar.append(input("Ingrese primera letra: ").lower()) #con este codigo indicamos que el input se agregue a un apendice
letras_a_buscar.append(input("Ingrese tercera letra: ").lower()) #con lower hacemos que lo que ingrese el ususario sea transformadoen minusculas
letras_a_buscar.append(input("Ingrese tercera letra: ").lower()) 

print("\nLa cantidad de letras encontradas segun el ingreso del ususario son :")

cantidad_de_letras_1 = texto_en_minusculas.count(letras_a_buscar[0]) #con este codigo buscamos el en el texto en minusculas cuantas veces se encuentra la primera letra del indice letras a buscar
cantidad_de_letras_2 = texto_en_minusculas.count(letras_a_buscar[1]) #este el segundo
cantidad_de_letras_3 = texto_en_minusculas.count(letras_a_buscar[2]) #este el tercero

print(f"\nEncontramos la letra '{letras_a_buscar[0]}', {cantidad_de_letras_1} veces")
print(f"Encontramos la letra '{letras_a_buscar[1]}', {cantidad_de_letras_2} veces")
print(f"Encontramos la letra '{letras_a_buscar[2]}', {cantidad_de_letras_3} veces")

#aca comenzaremos con la 2da parte
texto_listado = texto_en_minusculas.split() #aca convertimos el texto en una lista
print(f"\nExiste un total de {len(texto_listado)} palabras en el texto.") #aca imprimimos el texto y a la vez lo contamos en la misma funcion

#aca comenzaremos la 3ra parte
primera_letra_texto = texto_en_minusculas[0] #aca definimos que la variable primera_letra contiene el texto indexado en el caracter 0
ultima_letra_texto = texto_en_minusculas[-1] #aca lo mismo pero en el caracter -1 que si recordamos es orden inverso
print(f"\nLa letra '{primera_letra_texto}', es la primera letra en el texto")
print(f"La letra '{ultima_letra_texto}', es la ultima letra del texto\n")

#aca comienza la 4ta parte
print("Este es el texto invertido y sin espacios: \n")
texto_invertido = texto_en_minusculas[::-1] #con esta funcion invertimos el texto
texto_invertido_junto = texto_invertido.replace(" ","") #con esta funcion quitamos los espacios en el texto
print(texto_invertido_junto) 

#aca comienza la 5ta y ultima parte
print("\nExiste la palabra Python en el texto?")
pregunta = "Python" in texto
diccionario = {True:"Si", False:"No"} #aca creamos un diccionario donde definimos que significan los parametros True o False
print(f"La palabra 'Python' {diccionario[pregunta]} se encuentra en el texto.") #en este codigo imprimimos el contenido de diccionario (True=Si False=No) segun la respuesta de la variable pregunta