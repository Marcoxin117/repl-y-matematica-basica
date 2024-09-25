# STRINGS 
# se puede poner con millas dobles "" O comillas simples '' 
mi_first_string = "mi string con comillas dobles"
mi_second_string = 'mi string con comillas simples'

#print (mi_first_string, mi_second_string)

print (f'esto es un texto de una variable {mi_second_string} rico') # se le agrega una f para poder agregar strings 

other_string = 'hola'
 
a,b,c,d = other_string 

print(a)
print(b)
print(c)
print(d)    

print (f'{a}{b}{c}{d}')

print (mi_first_string.upper()) #poner un punto . despues de la variable da diferentes acciones
print (mi_first_string.capitalize()) 
print (mi_first_string.lower())
print (len(mi_first_string))
print (mi_first_string.find('i'))
print (mi_first_string.count('i')) # count es para saber cuantas i hay en el string
print (mi_first_string.upper().isupper()) # con is pregunta si todo es upper lo cual sera cierto 
